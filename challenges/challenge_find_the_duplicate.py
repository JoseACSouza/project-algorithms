def find_duplicate(nums):
    if len(nums) < 2:
        return False
    contagem = {}

    for num in nums:
        if type(num) is not int or num < 0:
            return False
        elif num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 0
    verifyDuplicate = max(contagem.values()) > 0
    max_number = max(contagem, key=contagem.get)
    numero_mais_repetido = max_number if verifyDuplicate else False

    return numero_mais_repetido
