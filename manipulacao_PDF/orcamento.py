from fpdf import FPDF

pdf = FPDF()


#Entrada de dados (quantidade de horas, valor por hora, quantidade de dias, valor por dia)
horas = int(input('Digite o total de horas: '))
valor_hora = int(input('Digite o valor por hora: '))
prazo = int(input('Digite o prazo (dias): '))
diaria = int(input('Digite o valor por hora: '))

#cálculos do valor total de horas e diárias
total_horas = valor_hora * horas
total_dias = diaria * prazo
valor_total = total_horas + total_dias

#Gerando o PDF, informando a fonte e incluindo o template
pdf.add_page()
pdf.set_font("Arial", size=12)  
pdf.image("Orcamento_empty.png", x=0, y=0)

#escrevendo no pdf as coordenadas e valores referentes as horas
pdf.text(112, 122, str(horas))  
pdf.text(135, 122, ("R$"+ str(valor_hora) +",00"))  
pdf.text(162, 122, ("R$"+ str(total_horas) +",00"))  

#escrevendo no pdf as coordenadas e valores referentes aos dias
pdf.text(112, 135, str(prazo))  
pdf.text(135, 135, ("R$"+ str(diaria) +",00"))  
pdf.text(162, 135, ("R$"+ str(total_dias) +",00"))  

#escrevendo no pdf as coordenadas e valor total da proposta
pdf.text(162, 203, ("R$"+ str(valor_total) +",00")) 

#aviso de tarefa finalizada
print("PDF armazenado")

#Este será o nome do PDF
pdf.output("Orcamento.pdf")