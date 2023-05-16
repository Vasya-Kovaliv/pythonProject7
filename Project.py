def s_block(input_data, s_table):
    output_data = []
    for i in input_data:
        output_data.append(s_table[i])
    return output_data

def inverse_Sblock(input_data, s_table_inverse):
    output_data = []
    for i in input_data:
        output_data.append(s_table_inverse[i])
    return output_data

def p_block(input_data, permutation_table):
    output_data = []
    for i in permutation_table:
        output_data.append(input_data[i])
    return output_data

def inverse_pBlock(input_data, permutation_table_inverse):
    output_data = [0] * len(input_data)
    for i, value in enumerate(permutation_table_inverse):
        output_data[value] = input_data[i]
    return output_data

def test_s_block():
    input_data = [0, 1, 2, 3]
    s_table = [1, 3, 0, 2]
    expected_output = [1, 3, 0, 2]

    assert s_block(input_data, s_table) == expected_output

    s_table_inverse = [2, 0, 3, 1]
    assert inverse_Sblock(expected_output, s_table_inverse) == input_data

    print("Тест S-блоку пройдено успішно.")

def test_p_block():
    input_data = [0, 1, 2, 3]
    permutation_table = [3, 0, 1, 2]
    expected_output = [3, 0, 1, 2]

    # Перевірка прямого перетворення
    p_block_output = p_block(input_data, permutation_table)
    print("Пряме перетворення P-блоку:")
    print("Input       :", input_data)
    print("Output      :", p_block_output)
    print("Expected    :", expected_output)

    # Перевірка зворотного перетворення
    permutation_table_inverse = [1, 2, 3, 0]
    inverse_p_block_output = inverse_pBlock(p_block_output, permutation_table_inverse)
    print("Зворотне перетворення P-блоку:")
    print("Input       :", p_block_output)
    print("Output      :", inverse_p_block_output)
    print("Expected    :", input_data)
    assert p_block_output== expected_output
    assert set(inverse_p_block_output) == set(input_data)
    print("Тест P-блоку пройдено успішно.")

test_s_block()
test_p_block()
