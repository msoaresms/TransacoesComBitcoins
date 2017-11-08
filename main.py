import re

primeiraVezUsuario = "True"
primeiraVezCpf = "True"


def validarCpf(cpf, entrada):
    global primeiraVezCpf
    digitos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    digitos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    j = 0
    soma = j
    for i in digitos1:
        soma = (i * cpf[j]) + soma
        j = j + 1

    soma = (soma % 11)
    if soma < 2:
        digito1 = 0
    else:
        digito1 = 11 - soma

    j = 0
    soma = j
    for i in digitos2:
        soma = (i * cpf[j]) + soma
        j = j + 1

    soma = (soma % 11)
    if soma < 2:
        digito2 = 0
    else:
        digito2 = 11 - soma

    if digito1 == cpf[9] and digito2 == cpf[10]:
        if primeiraVezCpf == "True":
            primeiraVezCpf = "False"
            modalidade(entrada)
        else:
            validarBitcoins(entrada)
    else:
        print("False")


def validarCnpj(cnpj, entrada):
    global primeiraVezCpf
    digitos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digitos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    j = 0
    soma = j
    for i in digitos1:
        soma = (i * cnpj[j]) + soma
        j = j + 1

    soma = (soma % 11)
    if soma < 2:
        digito1 = 0
    else:
        digito1 = 11 - soma

    j = 0
    soma = j
    for i in digitos2:
        soma = (i * cnpj[j]) + soma
        j = j + 1

    soma = (soma % 11)
    if soma < 2:
        digito2 = 0
    else:
        digito2 = 11 - soma

    if digito1 == cnpj[12] and digito2 == cnpj[13]:
        validarBitcoins(entrada)
    else:
        print("False")


def validacao(entrada):
    loginUsuario(entrada)


def loginUsuario(entrada):
    global primeiraVezUsuario
    if primeiraVezUsuario == "True":
        primeiraVezUsuario = "False"
        if re.match(r'^[a-z]{1}([a-z]|[A-Z]){0,}$', entrada[0]):
            cpfUsuario(entrada)
        else:
            print("False")
    else:
        if re.match(r'^[a-z]{1}([a-z]|[A-Z]){0,59}$', entrada[3]):
            cpfUsuario(entrada)
        else:
            print("False")


def cpfUsuario(entrada):
    global primeiraVezCpf
    if primeiraVezCpf == "True":
        if re.match(r'^([0-9]{3}[.]){2}[0-9]{3}[-][0-9]{2}$', entrada[1]):
            string = entrada[1].replace(".", "")
            string = string.replace("-", "")
            cpf = re.findall('.', string)
            cpfInt = [int(x) for x in cpf]
            validarCpf(cpfInt, entrada)
        else:
            print("False")
    else:
        if re.match(r'^([0-9]{3}[.]){2}[0-9]{3}[-][0-9]{2}$', entrada[4]):
            string = entrada[4].replace(".", "")
            string = string.replace("-", "")
            cpf = re.findall('.', string)
            cpfInt = [int(x) for x in cpf]
            validarCpf(cpfInt, entrada)
        else:
            print("False")


def validarBitcoins(entrada):
    valorBitcoins = entrada[5] + " " + entrada[6]
    if re.match(r'^[B][$][ ][0-9]*[.][0-9]{2}$', valorBitcoins):
        if re.match(r'^R[$]$', entrada[7]):
            validarComplemento(entrada)
        else:
            validarHash(entrada, 2)
    else:
        print("False")


def validarComplemento(entrada):
    valorComplemento = entrada[7] + " " + entrada[8]
    if re.match(r'^[R][$][ ][0-9]*[.][0-9]{2}$', valorComplemento):
        validarHash(entrada, 1)
    else:
        print("False")


def banco(entrada):
    if re.match(r'^(brasil|caixa|itau|bradesco|safra|outro)$', entrada[3]):
        cnpj(entrada)
    else:
        print("False")


def cnpj(entrada):
    if re.match(r'^[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}$', entrada[4]):
        string = entrada[4].replace(".", "")
        string = string.replace("-", "")
        string = string.replace("/", "")
        cnpjEmpresa = re.findall('.', string)
        cnpjInt = [int(x) for x in cnpjEmpresa]
        validarCnpj(cnpjInt, entrada)
    else:
        print("False")


def modalidade(entrada):
    if re.match(r'^user$', entrada[2]):
        loginUsuario(entrada)
    elif re.match(r'^bank$', entrada[2]):
        banco(entrada)
    else:
        print("False")


def validarHash(entrada, opcao):
    if opcao == 1:
        if re.match(r'^([0-9]|[a-f]){32}$', entrada[9]):
            print("True")
        else:
            print("False")
    else:
        if re.match(r'^([0-9]|[a-f]){32}$', entrada[7]):
            print("True")
        else:
            print("False")


entrada = input()
entrada2 = entrada.split()

if len(entrada2) < 8 or 8 < len(entrada2) < 10:
    print("False")
else:
    validacao(entrada2)


