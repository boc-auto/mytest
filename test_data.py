import pytest
import yaml


# def get_yaml(filepath):
#     f = open(filepath)
#     data = yaml.safe_load_all(f)
#     return data

# m0 = list(get_yaml('data_list.yaml'))
# print(m0[0])

# m1 = list(get_yaml('data_dict.yaml'))
# print(m1[0])

# m2 = list(get_yaml('data_list_nesting.yaml'))
# print(m2[0][0])

# m3 = list(get_yaml('data_array.yaml'))
# print(m3[0][0])

# m4 = list(get_yaml('data_nesting.yaml'))
# print(m4[0]['companies'][0])

# m = list(yaml.safe_load_all(open('./data_test.yaml')))
# print(m[0])
class TestDemo:

    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open('./data_test.yaml')))
    def test_one(self, a, b):
        print(a + b)










