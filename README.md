# Conllu-File-Comparator
Programa em Python que compara as relações de dependência "nsubj", "csubj", "obj" e "iobj" entre um arquivo ".conllu" de teste e outro ".conllu" de referência.

O objetivo do programa é verificar a acurácia de um parser de dependências em relação a um arquivo de referência (anotação correta das sentenças), calculando a *precisão*, *cobertura*, *medida-f* e *desvio padrão da precisão e da cobertura* com relação a quatro relações de dependência: [**nsubj**](https://universaldependencies.org/en/dep/nsubj.html), [**csubj**](https://universaldependencies.org/en/dep/csubj.html), [**obj**](https://universaldependencies.org/u/dep/obj.html) e [**iobj**](https://universaldependencies.org/u/dep/iobj.html).

### Biblioteca *conllu* do Python

O parser CoNLL-U analisa um arquivo formatado em [CoNLL-U](https://universaldependencies.org/format.html) em um Python [dictionary](https://www.w3schools.com/python/python_dictionaries.asp). CoNLL-U geralmente é o formato padrão de saída de parsers de dependência em processamento de linguagem natural.

É necessário que essa biblioteca esteja instalada no computador do usuário para que ele possa executar o programa. Para instalar a biblioteca, basta executar o seguinte comando no terminal:<br>
```
pip3 install conllu
```

### Execução do programa

O usuário deve fazer o download do `.zip` da pasta do repositório e descompactar. Para comparar os dois arquivos `.conllu` o usuário deve colocar os arquivos dentro da pasta descompactada do repositório e abrir o terminal dentro desse repositório (referenciando o repositório). Após isso, é só executar o programa inserindo o seguinte comando no terminal:<br>
```
python3 conllu_file_comparator.py
```

Ao iniciar a execução, o programa irá solicitar o nome do arquivo de referência (Ex: referencia.conllu) e, em seguida, o nome do arquivo de teste (Ex: teste.conllu).

O programa deverá dar uma saída no formato do resultado a seguir, exibindo a quantidade e as medidas precisão, cobertura, medida-f e desvio padrão das medidas precisão e cobertura de cada relação core (subj, csubj, obj e iobj):
```
RELATION "nsubj"

Number of relations "nsubj" in test corpus:  517
Precision:  0.482774752129591
Recall:  0.4637883008356547
F-measure:  0.4730911084583783
Standard Deviation (Precision):  0.45746580432209805
Standard Deviation (Recall):  0.4615394258979827
---------------------------
RELATION "csubj"

Number of relations "csubj" in test corpus:  3
Precision:  1.0
Recall:  0.2777777777777778
F-measure:  0.4347826086956522
Standard Deviation (Precision):  0.0
Standard Deviation (Recall):  0.41573970964154905
---------------------------
RELATION "obj"

Number of relations "obj" in test corpus:  435
Precision:  0.535705596107056
Recall:  0.4774477447744775
F-measure:  0.5049017131046266
Standard Deviation (Precision):  0.4531379383644991
Standard Deviation (Recall):  0.4552742844836239
---------------------------
RELATION "iobj"

Number of relations "iobj" in test corpus:  11
Precision:  0.3333333333333333
Recall:  0.09615384615384616
F-measure:  0.14925373134328357
Standard Deviation (Precision):  0.4714045207910317
Standard Deviation (Recall):  0.2780160056692492
---------------------------
```

