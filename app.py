from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import os
from datetime import datetime
import json

app = Flask(__name__, static_folder='static', template_folder='static')

# 存储测试结果
test_reports = []


def run_test(test_file):
    """运行指定的测试文件并返回结果"""
    try:
        result = subprocess.run(
            [sys.executable, f"payment_testcase/{test_file}"],
            capture_output=True,
            text=True
        )
        return {
            "success": True,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-tests', methods=['POST'])
def run_tests():
    test_type = request.json.get('test_type')
    test_files = []

    if test_type == 'All':
        test_files = ['test_id.py', 'test_my.py', 'test_th.py', 'test_vn.py']
    elif test_type == 'Indonesia':
        test_files = ['test_id.py']
    elif test_type == 'Malaysia':
        test_files = ['test_my.py']
    elif test_type == 'Thailand':
        test_files = ['test_th.py']
    elif test_type == 'Vietnam':
        test_files = ['test_vn.py']
    else:
        return jsonify({"error": "Invalid test type"}), 400

    results = []
    for test_file in test_files:
        result = run_test(test_file)
        results.append({
            "test_file": test_file,
            "result": result
        })

    # 创建报告
    report = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "test_type": test_type,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    }

    test_reports.append(report)

    return jsonify(report)


@app.route('/get-reports', methods=['GET'])
def get_reports():
    return jsonify(test_reports)


@app.route('/get-report/<report_id>', methods=['GET'])
def get_report(report_id):
    for report in test_reports:
        if report['id'] == report_id:
            return jsonify(report)
    return jsonify({"error": "Report not found"}), 404


if __name__ == '__main__':
    app.run(debug=False)