from pathlib import Path
import json

from filetools import csv_to_json, json_to_csv, read_csv, read_json, write_json


def test_read_csv_from_temp_file(tmp_path):
    sample_csv = tmp_path / "sample.csv"
    sample_csv.write_text("name,grade\nAlice,92\nBob,85\n", encoding="utf-8")

    rows = read_csv(str(sample_csv))

    assert isinstance(rows, list)
    assert rows == [{"name": "Alice", "grade": "92"}, {"name": "Bob", "grade": "85"}]


def test_read_json_from_temp_file(tmp_path):
    sample_json = tmp_path / "sample.json"
    payload = [{"name": "Alice", "grade": 92}]
    sample_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    data = read_json(str(sample_json))

    assert data == payload


def test_write_json_and_read_back(tmp_path):
    payload = [{"name": "Zoe", "grade": 100}]
    out_path = tmp_path / "out.json"

    write_json(str(out_path), payload)

    with open(out_path, encoding="utf-8") as f:
        assert json.load(f) == payload


def test_csv_to_json_type_conversion(tmp_path):
    sample_csv = tmp_path / "sample.csv"
    sample_csv.write_text("name,grade\nAlice,92\nBob,85\n", encoding="utf-8")
    json_path = tmp_path / "converted.json"

    csv_to_json(str(sample_csv), str(json_path), type_hints={"grade": int})
    converted = read_json(str(json_path))

    assert converted == [{"name": "Alice", "grade": 92}, {"name": "Bob", "grade": 85}]


def test_json_to_csv_fieldnames(tmp_path):
    sample_json = tmp_path / "source.json"
    payload = [
        {"name": "Alice", "grade": 92, "email": "alice@uni.edu"},
        {"name": "Bob", "grade": 85, "club": "robotics"},
    ]
    sample_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    csv_path = tmp_path / "output.csv"
    json_to_csv(str(sample_json), str(csv_path), ["name", "grade", "email"])

    rows = read_csv(str(csv_path))
    assert rows == [
        {"name": "Alice", "grade": "92", "email": "alice@uni.edu"},
        {"name": "Bob", "grade": "85", "email": ""},
    ]
