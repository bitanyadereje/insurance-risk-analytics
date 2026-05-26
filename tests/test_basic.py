import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    from src import data_loader, eda_utils, hypothesis_tests, modeling
    assert True
