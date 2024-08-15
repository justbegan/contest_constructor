import ast


def convert_parameter(parameter: dict):
    """
    Кастыль для фронта
    """
    try:
        parameter_copy = parameter.copy()
        key, value = parameter_copy.popitem()
        converted_dict = ast.literal_eval(value)
        return {
            key: converted_dict
        }
    except:
        return parameter
