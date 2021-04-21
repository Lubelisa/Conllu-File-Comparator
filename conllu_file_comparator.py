from conllu import parse
from statistics import pstdev

#  TOKEN: dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc'])

def reinit_corerelations_listdict():
	core_relations_list = {
	'nsubj' : [],
	'csubj' : [],
	'obj' : [],
	'iobj' : []
	}
	return core_relations_list

def reinit_corerelations_intdict():
	core_relations_int = {
	'nsubj' : 0,
	'csubj' : 0,
	'obj' : 0,
	'iobj' : 0
	}
	return core_relations_int

# Lendo e processando o conllu do bosque anotado manualmente.
name_file = str(input('Digite o nome do arquivo .conllu de referencia (ex: file.conllu): '))
data_reference = open(name_file, 'r', encoding='utf-8').read()
data_reference_tokenlist = parse(data_reference)

# Lendo e processando o conllu do bosque anotado pelo parse a ser analisado.
name_file = str(input('Digite o nome do arquivo .conllu de teste (ex: file.conllu): '))
data_test = open(name_file, 'r', encoding='utf-8').read()
data_test_tokenlist = parse(data_test)

'''
Procurar entre os tokens de cada sentença do 'data_reference' as relações presentes na lista 'core_relations'
e verificar se elas estão corretas. 
'''

# Contagem da precisão
dict_precision_values = reinit_corerelations_listdict()

# Contagem da cobertura
dict_recall_values = reinit_corerelations_listdict()

# Contagem do número de sentenças de referencia que foram encontradas relações de cada tipo
dict_sentence_rel = reinit_corerelations_listdict()

#Contagem do número de relações core no córpus de teste
dict_count_core_relations = reinit_corerelations_intdict()



for i in range(len(data_reference_tokenlist)):
	# Recuperando as relações core presentes na sentença de referência

	core_relations_refsent = reinit_corerelations_listdict() # Armazenar as relações core presentes na sentença de referencia
	core_relations_testsent_present = reinit_corerelations_intdict() # Armazenar o número de relações presentes na sent de teste
	core_relations_testsent_correct = reinit_corerelations_intdict() # Armazenar o número de relações corretas das presentes na sent de teste

	sentence = data_reference_tokenlist[i]
	for j in range(len(sentence)):
		token = sentence[j]
		if token['deprel'] in core_relations_refsent.keys():
			dest = token['form'].lower()
			org = sentence[token['head']-1]
			org = org['form'].lower()
			core_relations_refsent[token['deprel']].append((dest, org))

	# Comparando as relações core da sentença de teste com as de referência, caso existam
	if(i < len(data_test_tokenlist)):
		sentence = data_test_tokenlist[i]
		for j in range(len(sentence)):
			token = sentence[j]
			if token['deprel'] in core_relations_refsent.keys() and len(core_relations_refsent[token['deprel']]) > 0:
				core_relations_testsent_present[token['deprel']]+=1
				dest = token['form'].lower()
				org = sentence[token['head']-1]
				org = org['form'].lower()
				dict_count_core_relations[token['deprel']]+=1
				if (dest, org) in core_relations_refsent[token['deprel']]:
					core_relations_testsent_correct[token['deprel']]+=1

	# Calculando as medidas e colocando nas respectivas listas
	for key_ in dict_precision_values.keys():

		if len(core_relations_refsent[key_]) > 0:
			dict_recall_values[key_].append(core_relations_testsent_correct[key_]/len(core_relations_refsent[key_]))

		if core_relations_testsent_present[key_] > 0:
			dict_precision_values[key_].append(core_relations_testsent_correct[key_]/core_relations_testsent_present[key_])

		if core_relations_testsent_correct[key_] > 0:
			dict_sentence_rel[key_].append(core_relations_testsent_correct[key_])
			

'''
Tendo então verificado as relações, pode-se calcular a precisão, cobertura, medida-f e desvio padrão das medidas do 
arquivo de teste.
'''

for key_ in dict_precision_values.keys():

	precision = sum(dict_precision_values[key_])/len(dict_precision_values[key_]) if len(dict_precision_values[key_]) > 0 else 0.0
	recall = sum(dict_recall_values[key_])/len(dict_recall_values[key_]) if len(dict_recall_values[key_]) > 0 else 0.0
	fmeasure = (2*precision*recall)/(precision+recall)

	sd_precision = pstdev(dict_precision_values[key_])
	sd_recall = pstdev(dict_recall_values[key_])

	print('RELATION \"'+str(key_)+'\"')
	print()
	print('Number of relations \"'+str(key_)+'\" in test corpus: ', dict_count_core_relations[key_])
	print('Precision: ', precision)
	print('Recall: ', recall)
	print('F-measure: ', fmeasure)

	print('Standard Deviation (Precision): ', sd_precision)
	print('Standard Deviation (Recall): ', sd_recall)
	print('---------------------------')


