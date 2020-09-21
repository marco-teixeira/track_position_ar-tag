import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from time import sleep

# New Antecedent/Consequent objects hold universe variables and membership
# functions
entradaY = ctrl.Antecedent(np.arange(-180, 180, 0.1), 'DistanciaY')
saidaAngular = ctrl.Consequent(np.arange(-0.8,0.8, 0.005), 'velocidadeAngular')

endtradaX = ctrl.Antecedent(np.arange(0, 10, 0.5), 'DistanciaX')
saidaLinear = ctrl.Consequent(np.arange(0,0.3, 0.005), 'velocidadeLinear')


# Auto-membership function population is possible with .automf(3, 5, or 7)
endtradaX["Muito Perto"] = fuzz.trapmf(endtradaX.universe, [-10, -5, 0, 0.8]);
endtradaX["Perto"] = fuzz.trimf(endtradaX.universe, [0.4, 0.8, 1.2,]);
endtradaX["Longe"] =fuzz.trapmf(endtradaX.universe, [0.8, 1.2, 10.0, 10.0]);



# Auto-membership function population is possible with .automf(3, 5, or 7)
entradaY["Muito Esquerda"] = fuzz.trapmf(entradaY.universe, [-180, -180, -90, -45]);
entradaY["Esquerda"] = fuzz.trimf(entradaY.universe, [-90, -45, 0]);
entradaY["Centro"] = fuzz.trimf(entradaY.universe, [ -45, 0,45]);
entradaY["Direita"] =fuzz.trimf(entradaY.universe, [ 0,45,90]);
entradaY["Muito Direita"] =   fuzz.trapmf(entradaY.universe, [45, 90,180, 180]);
#entradaY.view()

#Criando as saidas:
saidaAngular.automf(5)
saidaLinear.automf(3)
#saidaAngular.view();
#

# Custom membership functions can be built interactively with a familiar,
# Pythonic API


# You can see how these look with .view()


#endtradaLinear.view()
#tip.view()

rule1 = ctrl.Rule(entradaY['Muito Esquerda'], saidaAngular['poor'])
rule2 = ctrl.Rule(entradaY['Esquerda'], saidaAngular['mediocre'])
rule3 = ctrl.Rule(entradaY['Centro'], saidaAngular['average'])
rule4 = ctrl.Rule(entradaY['Direita'], saidaAngular['decent'])
rule5 = ctrl.Rule(entradaY['Muito Direita'], saidaAngular['good'])


rule6 = ctrl.Rule((endtradaX['Muito Perto'] & entradaY['Muito Esquerda']),  saidaLinear['poor'])
rule7 = ctrl.Rule((endtradaX['Muito Perto'] & entradaY['Muito Direita']),  saidaLinear['poor'])
rule8 = ctrl.Rule((endtradaX['Muito Perto'] & entradaY['Esquerda']),  saidaLinear['poor'])
rule9 = ctrl.Rule((endtradaX['Muito Perto'] & entradaY['Direita']),  saidaLinear['poor'])
rule10 = ctrl.Rule((endtradaX['Muito Perto'] & entradaY['Centro']),  saidaLinear['poor'])


rule11 = ctrl.Rule((endtradaX['Perto'] & entradaY['Muito Esquerda']),  saidaLinear['poor'])
rule12 = ctrl.Rule((endtradaX['Perto'] & entradaY['Muito Direita']),  saidaLinear['poor'])
rule13 = ctrl.Rule((endtradaX['Perto'] & entradaY['Esquerda']),  saidaLinear['poor'])
rule14 = ctrl.Rule((endtradaX['Perto'] & entradaY['Direita']),  saidaLinear['poor'])
rule15 = ctrl.Rule((endtradaX['Perto'] & entradaY['Centro']),  saidaLinear['average'])



rule16 = ctrl.Rule((endtradaX['Longe'] & entradaY['Muito Esquerda']),  saidaLinear['poor'])
rule17 = ctrl.Rule((endtradaX['Longe'] & entradaY['Muito Direita']),  saidaLinear['poor'])
rule18 = ctrl.Rule((endtradaX['Longe'] & entradaY['Esquerda']),  saidaLinear['poor'])
rule19 = ctrl.Rule((endtradaX['Longe'] & entradaY['Direita']),  saidaLinear['poor'])
rule20 = ctrl.Rule((endtradaX['Longe'] & entradaY['Centro']),  saidaLinear['good'])

#rule1.view()
#rule2.view()
#rule2.view()

#Control
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20])
#input("Pressione <enter> para continuar")





