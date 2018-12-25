# -*- coding: utf-8 -*-
import random as r
import webbrowser
import speech
import sound
import time
import ui

"""
View view_menu_principal. Affiche 4 boutons et 1 texte, le bouton 1 permet de lancer l'éthylomètre, le bouton 2 permet de lancer le generateur de calcul, le bouton 3 permet de lancer le test avec les hexagones et le bouton 4 permet d'ouvrir une page Soundcloud.
"""

def button_1_menu_principal(sender):
	"""
	button_1_menu_principal : sender -> None
	button_1_menu_principal(sender) ajoute la sous-vue view_genre à la vue view_menu_principal, return None.
	"""
	global view_menu_principal
	global view_genre
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_menu_principal.add_subview(view_genre)
	
	return None
	
	
def button_2_menu_principal(sender):
	"""
	button_2_menu_principal : sender -> None
	button_2_menu_principal(sender) si le test n'a pas encore été effectué, ajoute la sous-vue view_preparation_generateur_de_calcul à la vue view_menu_principal, sinon, joue un effet sonore, return None.
	"""
	global view_menu_principal
	global view_preparation_generateur_de_calcul
	global duree_execution_generateur_de_calcul
	
	if duree_execution_generateur_de_calcul == 1: # Si le jeu n'a pas été éxécuté.
		sound.play_effect('Bottle open sound.m4a')
		view_menu_principal.add_subview(view_preparation_generateur_de_calcul)
	
	else:
		sound.play_effect('game:Error')
		
	return None

		
def button_3_menu_principal(sender):
	"""
	button_3_menu_principal : sender -> None
	button_3_menu_principal(sender) si le test n'a pas encore été effectué, ajoute la sous-vue view_preparation_jeu_hexagones à la vue view_menu_principal, sinon, joue un effet sonore, return None.
	"""
	global view_menu_principal
	global view_preparation_jeu_hexagones
	global duree_execution_jeu_hexagones

	if duree_execution_jeu_hexagones == 1: # Si le jeu n'a pas été éxécuté.
		sound.play_effect('Bottle open sound.m4a')
		view_menu_principal.add_subview(view_preparation_jeu_hexagones)
	
	else:
		sound.play_effect('game:Error')
	
	return None
	
	
def button_4_menu_principal(sender):
	"""
	button_4_menu_principal : sender -> None
	button_4_menu_principal(sender) ajoute la sous-vue view_soundcloud_calculatrice à la vue view_menu_principal, return None.
	"""
	global view_menu_principal
	global view_soundcloud_calculatrice
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_menu_principal.add_subview(view_soundcloud_calculatrice)
	
	return None
	
	
"""
View Genre. Permet à l'utilisateur de saisir son genre. En fonction du genre selectionné, change la valeur assignée à la variable coefficient_de_diffusion_k, et ajoute la sous-vue view_calculatrice_poids.
"""

def button_soundcloud_calculatrice(sender):
	"""
	button_soundcloud_calculatrice : sender -> None
	button_soundcloud_calculatrice(sender) ajoute la sous-vue view_soundcloud_calculatrice, return None.
	"""
	global view_genre
	global view_soundcloud_calculatrice
	
	view_genre.add_subview(view_soundcloud_calculatrice)
	
	return None
	
	
def button_homme_calculatrice(sender):
	"""
	button_homme_calculatrice : sender -> None
	button_homme_calculatrice(sender) implémente la liste coefficient_de_diffusion du terme coefficient_de_diffusion_homme, return None.
	"""
	global view_genre
	global view_calculatrice_poids
	global label_genre_calculatrice
	global coefficient_de_diffusion_k	
	
	if label_genre_calculatrice.text == 'Vous êtes ?':
		sound.play_effect('ApplePay sound effect.m4a')
		coefficient_de_diffusion_homme = 0.7
		coefficient_de_diffusion_k += coefficient_de_diffusion_homme
		view_genre.add_subview(view_calculatrice_poids)
		
	else:
		pass
		
	return None
	
	
def button_femme_calculatrice(sender):
	"""
	button_femme_calculatrice : sender -> None
	button_femme_calculatrice(sender) implémente la liste coefficient_de_diffusion du terme coefficient_de_diffusion_femme, return None.
	"""
	global view_genre
	global view_calculatrice_poids
	global label_genre_calculatrice
	global coefficient_de_diffusion_k
	
	if label_genre_calculatrice.text == 'Vous êtes ?':
		sound.play_effect('ApplePay sound effect.m4a')
		coefficient_de_diffusion_femme = 0.6
		coefficient_de_diffusion_k += coefficient_de_diffusion_femme
		view_genre.add_subview(view_calculatrice_poids)
		
	else:
		pass
		
	return None
	
	
"""
View Soundcloud. Charge et affiche une page Soundcloud, afin de séléctionner de la musique lors de l'éxécution du programme. Une croix est disponible dans l'angle superieur gauche, et permet d'enlever la page de l'affichage tout en gardant son contenu chargé en arrière-plan.
"""

def button_retour_calculatrice(sender):
	"""
	button_retour_calculatrice : sender -> None
	button_retour_calculatrice(sender) retire la sous-vue view_souncloud_calculatrice, return None.
	"""
	global view_genre
	global view_soundcloud_calculatrice
	
	view_genre.remove_subview(view_soundcloud_calculatrice)
	
	return None
	
	
"""
View Poids. Permet à l'utilisateur d'entrer son poids en kg, le bouton ok permet de lancer la suite du programme par l'affichage de la sous-vue view_classes, le poids saisi ne peut etre superieur à 999. Le poids est affecté à la variable globale poids_utilisateur.
"""

def button_1_calculatrice(sender):
	"""
	button_1_calculatrice : Sender -> None
	button_1_calculatrice(sender) ajoute la valeur 1 a la liste liste_calculatrice et ajoute 1 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '1'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_2_calculatrice(sender):
	"""
	button_2_calculatrice : Sender -> None
	button_2_calculatrice(sender) ajoute la valeur 2 a la liste liste_calculatrice et ajoute 2 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '2'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		pass
		
	return None
	
	
def button_3_calculatrice(sender):
	"""
	button_3_calculatrice : Sender -> None
	button_3_calculatrice(sender) ajoute la valeur 3 a la liste liste_calculatrice et ajoute 3 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '3'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_4_calculatrice(sender):
	"""
	button_4_calculatrice : Sender -> None
	button_4_calculatrice(sender) ajoute la valeur 4 a la liste liste_calculatrice et ajoute 4 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '4'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_5_calculatrice(sender):
	"""
	button_5_calculatrice : Sender -> None
	button_5_calculatrice(sender) ajoute la valeur 5 a la liste liste_calculatrice et ajoute 5 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '5'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_6_calculatrice(sender):
	"""
	button_6_calculatrice : Sender -> None
	button_6_calculatrice(sender) ajoute la valeur 6 a la liste liste_calculatrice et ajoute 6 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '6'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_7_calculatrice(sender):
	"""
	button_7_calculatrice : Sender -> None
	button_7_calculatrice(sender) ajoute la valeur 7 a la liste liste_calculatrice et ajoute 7 au texte du champs_de_texte_calculatrice, return None.
	
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '7'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_8_calculatrice(sender):
	"""
	button_8_calculatrice : Sender -> None
	button_8_calculatrice(sender) ajoute la valeur 8 a la liste liste_calculatrice et ajoute 8 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '8'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_9_calculatrice(sender):
	"""
	button_9_calculatrice : Sender -> None
	button_9_calculatrice(sender) ajoute la valeur 9 a la liste liste_calculatrice et ajoute 9 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '9'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_0_calculatrice(sender):
	"""
	button_0_calculatrice : Sender -> None
	button_0_calculatrice(sender) ajoute la valeur 0 a la liste liste_calculatrice et ajoute 0 au texte du champs_de_texte_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	if 0 < len(champs_de_texte_calculatrice.text) < 3:
		sound.play_effect('ui:mouseclick1')
		valeur = '0'
		liste_calculatrice.append(valeur)
		text_calculatrice = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = text_calculatrice
		
	else:
		None
		
	return None
	
	
def button_delete_calculatrice(sender):
	"""
	button_delete_generateur_de_calcul : sender -> None
	button_delete_generateur_de_calcul(sender) retire le dernier élément du Label principal et de la liste liste_calculatrice, return None.
	"""
	global champs_de_texte_calculatrice
	global liste_calculatrice
	
	sound.play_effect('ui:rollover2')
	
	len_liste_calculatrice = len(liste_calculatrice) 
	
	if len_liste_calculatrice != 0:
		del liste_calculatrice[len_liste_calculatrice - 1] # Retire le dernier élément de la liste.
		champs_de_texte_calculatrice_reduit = ''.join(liste_calculatrice)
		champs_de_texte_calculatrice.text = champs_de_texte_calculatrice_reduit
		
	else:
		None
		
	return None
	
	
def button_validation_calculatrice(sender):
	"""
	button_validation_calculatrice : sender -> None
	button_validation_calculatrice(sender) affecte la valeur du poids à la variable globale poids_utilisateur, charge la sous-vue view_classes, return None.
	"""
	global view_genre
	global view_calculatrice_poids
	global view_classes	
	global champs_de_texte_calculatrice
	global liste_calculatrice
	global poids_utilisateur
	
	len_champs_de_texte_calculatrice = len(champs_de_texte_calculatrice.text)
	
	if 1 < len_champs_de_texte_calculatrice < 4: # Pour filtrer les nombres supérieurs à 999.
	
		if  len_champs_de_texte_calculatrice != 0: # Si il y a un nombre saisi par l'utilisateur.
			sound.play_effect('ApplePay sound effect.m4a')
			int_poids_utilisateur = int(''.join(liste_calculatrice))
			poids_utilisateur += int_poids_utilisateur
			
			view_genre.add_subview(view_classes)
			view_genre.remove_subview(view_calculatrice_poids)
			
		else:
			None
			
	else:
		sound.play_effect('game:Error')
		
	return None
	
	
"""
View Classe alcool. Affiche la view classe alcool, l'utilisateur est ammené a selectionner la classe d'alcool qu'il a bu, entre bieres, spiritueux et vins. 3 boutons sont mis a disposition ainsi qu'une zone de texte. Ajoute la sous-vue view_marques_bieres ou view_categories_spiritueux ou view_categories_vins.
"""

def button_bieres_calculatrice(sender):
	"""
	button_bieres_calculatrice : sender -> None
	button_bieres_calculatrice(sender) ajoute la sous_vue view_marques_bieres, return None.
	"""
	global view_genre
	global view_marques_bieres
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_genre.add_subview(view_marques_bieres)

	return None

		
def button_spiritueux_calculatrice(sender):
	"""
	button_spiritueux_calculatrice : sender -> None
	button_spiritueux_calculatrice(sender) ajoute la sous_vue view_categories_spiritueux, return None.
	"""
	global view_genre
	global view_categories_spiritueux	
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_genre.add_subview(view_categories_spiritueux)
	
	return None

		
def button_vins_calculatrice(sender):
	"""
	button_vins_calculatrice : sender -> None
	button_vins_calculatrice(sender) ajoute la sous_vue view_categories_vins, return None.
	"""
	global view_genre
	global view_categories_vins	
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_genre.add_subview(view_categories_vins)
	
	return None
	
	
"""
View marques_bieres. Affiche 4 boutons, une zone de texte et un slider, le nom et la fonction des boutons changent en fonction de la valeur comprise entre 0 et 1, retournée par le slider. A l'appel de chaque bouton, affichage de  la sous-vue view_volumes_bieres, affectation de la valeur du degré alcoolique à la variable globale degre_alcoolique.
"""

def button_1_marques_bieres(sender):
	"""
	button_1_marques_bieres : sender -> None
	button_1_marques_bieres(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée à la variable degre_alcoolique, ajoute la sous_vue view_volumes_bieres, return None.
	"""
	global view_genre
	global view_marques_bieres
	global view_volumes_bieres
	global button_1_marques_bieres
	global slider_marques_bieres
	global degre_alcoolique
		
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_1_marques_bieres.title == 'Amsterdam':
		titre_alcoometrique_Amsterdam = 11.6
		degre_alcoolique += titre_alcoometrique_Amsterdam
		
	elif button_1_marques_bieres.title == 'Cubanisto':
		titre_alcoometrique_Cubanisto = 5.9
		degre_alcoolique += titre_alcoometrique_Cubanisto
		
	elif button_1_marques_bieres.title == 'Heineken':
		titre_alcoometrique_Heineken = 5.0
		degre_alcoolique += titre_alcoometrique_Heineken
		
	elif button_1_marques_bieres.title == 'Lager':
		titre_alcoometrique_Lager = 4.5
		degre_alcoolique += titre_alcoometrique_Lager
		
	elif button_1_marques_bieres.title == 'Rince Cochon':
		titre_alcoometrique_Rince_Cochon = 8.5
		degre_alcoolique += titre_alcoometrique_Rince_Cochon
		
		
	view_genre.add_subview(view_volumes_bieres)
	slider_marques_bieres.value = 0.0
	
	return None
	
	
def button_2_marques_bieres(sender):
	"""
	button_2_marques_bieres : sender -> None
	button_2_marques_bieres(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée à la variable degre_alcoolique, ajoute la sous_vue view_volumes_bieres, return None.
	"""
	global view_genre
	global view_marques_bieres
	global view_volumes_bieres
	global button_2_marques_bieres
	global slider_marques_bieres
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_2_marques_bieres.title == 'Atlas':
		titre_alcoometrique_Atlas = 7.2
		degre_alcoolique += titre_alcoometrique_Atlas
		
	elif button_2_marques_bieres.title == 'Desperados':
		titre_alcoometrique_Desperados = 5.9
		degre_alcoolique += titre_alcoometrique_Desperados
		
	elif button_2_marques_bieres.title == 'Kanterbrau':
		titre_alcoometrique_Kanterbrau = 4.6
		degre_alcoolique += titre_alcoometrique_Kanterbrau
		
	elif button_2_marques_bieres.title == 'La Goudale':
		titre_alcoometrique_La_Goudale = 7.2
		degre_alcoolique += titre_alcoometrique_La_Goudale
		
	elif button_2_marques_bieres.title == 'Skøll':
		titre_alcoometrique_Skoll = 6.0
		degre_alcoolique += titre_alcoometrique_Skoll
		
	view_genre.add_subview(view_volumes_bieres)
	slider_marques_bieres.value = 0.0
	
	return None
	
	
def button_3_marques_bieres(sender):
	"""
	button_3_marques_bieres : sender -> None
	button_3_marques_bieres(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée à la variable degre_alcoolique, ajoute la sous_vue view_volumes_bieres, return None.
	"""
	global view_genre
	global view_marques_bieres
	global view_volumes_bieres
	global button_3_marques_bieres
	global slider_marques_bieres
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_3_marques_bieres.title == 'Carlsberg':
		titre_alcoometrique_Carlsberg = 5.0
		degre_alcoolique += titre_alcoometrique_Carlsberg
		
	elif button_3_marques_bieres.title == 'Grimbergen':
		titre_alcoometrique_Grimbergen = 6.7
		degre_alcoolique += titre_alcoometrique_Grimbergen
		
	elif button_3_marques_bieres.title == 'Koenigsbier':
		titre_alcoometrique_Koenigsbier = 4.2
		degre_alcoolique += titre_alcoometrique_Koenigsbier
		
	elif button_3_marques_bieres.title == 'Leffe':
		titre_alcoometrique_Leffe = 6.5
		degre_alcoolique += titre_alcoometrique_Leffe
		
	elif button_3_marques_bieres.title == '86':
		titre_alcoometrique_86 = 6.5
		degre_alcoolique += titre_alcoometrique_86
		
	view_genre.add_subview(view_volumes_bieres)
	slider_marques_bieres.value = 0.0
	
	return None
	
	
def button_4_marques_bieres(sender):
	"""
	button_4_marques_bieres : sender -> None
	button_4_marques_bieres(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée à la variable degre_alcoolique, ajoute la sous_vue view_volumes_bieres, return None.
	"""
	global view_genre
	global view_marques_bieres
	global view_volumes_bieres
	global button_4_marques_bieres
	global slider_marques_bieres
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_4_marques_bieres.title == 'Corona':
		titre_alcoometrique_Corona = 4.6
		degre_alcoolique += titre_alcoometrique_Corona
		
	elif button_4_marques_bieres.title == 'Guiness':
		titre_alcoometrique_Guiness = 4.2
		degre_alcoolique += titre_alcoometrique_Guiness
		
	elif button_4_marques_bieres.title == 'Kronenbourg':
		titre_alcoometrique_Kronenbourg = 4.3
		degre_alcoolique += titre_alcoometrique_Kronenbourg
		
	elif button_4_marques_bieres.title == 'Pelfort':
		titre_alcoometrique_Pelfort = 5.6
		degre_alcoolique += titre_alcoometrique_Pelfort
		
	elif button_4_marques_bieres.title == '1664':
		titre_alcoometrique_1664 = 5.5
		degre_alcoolique += titre_alcoometrique_1664
		
	view_genre.add_subview(view_volumes_bieres)
	slider_marques_bieres.value = 0.0
	
	return None
	
	
def slider_marques_bieres(sender):
	"""
	slider_marques_bieres : sender -> None
	slider_marques_bieres(sender) modifie les titres des boutons de la sous-vue view_marques_bieres en fonction de la valeur retournée par le slider slider_marques_bieres, return None.
	"""
	global button_1_marques_bieres
	global button_2_marques_bieres
	global button_3_marques_bieres
	global button_4_marques_bieres
	global slider_marques_bieres
	
	
	if slider_marques_bieres.value < 0.20:
		button_1_marques_bieres.title = 'Amsterdam'
		button_2_marques_bieres.title = 'Atlas'
		button_3_marques_bieres.title = 'Carlsberg'
		button_4_marques_bieres.title = 'Corona'
		
	elif 0.20 <= slider_marques_bieres.value < 0.40:
		button_1_marques_bieres.title = 'Cubanisto'
		button_2_marques_bieres.title = 'Desperados'
		button_3_marques_bieres.title = 'Grimbergen'
		button_4_marques_bieres.title = 'Guiness'
		
	elif 0.40 <= slider_marques_bieres.value < 0.60:
		button_1_marques_bieres.title = 'Heineken'
		button_2_marques_bieres.title = 'Kanterbrau'
		button_3_marques_bieres.title = 'Koenigsbier'
		button_4_marques_bieres.title = 'Kronenbourg'
		
	elif 0.60 <= slider_marques_bieres.value < 0.80:
		button_1_marques_bieres.title = 'Lager'
		button_2_marques_bieres.title = 'La Goudale'
		button_3_marques_bieres.title = 'Leffe'
		button_4_marques_bieres.title = 'Pelfort'
		
	elif 0.80 <= slider_marques_bieres.value <= 1:
		button_1_marques_bieres.title = 'Rince Cochon'
		button_2_marques_bieres.title = 'Skøll'
		button_3_marques_bieres.title = '86'
		button_4_marques_bieres.title = '1664'
		
	return None

		
"""
View Volumes_bieres. Permet à l'utilisateur de selectionner le volume de boisson consommée, ainsi que le nombre de doses. ajoute la sous-vue view_boucle_calculatrice et affecte la valeur de la quantité d'alcool ingérée à la variable globale masse_alcool_totale.
"""

def slider_bouteilles(sender):
	"""
	slider_bouteilles : sender -> None
	slider_bouteilles(sender) modifie le texte du label label_nbre_bouteilles en fonction de la valeur retournée par le slider slider_bouteilles, return None.
	"""
	
	global slider_bouteilles
	global label_nbre_bouteilles
	
	if slider_bouteilles.value < 0.1:
		label_nbre_bouteilles.text = ''
		
	elif 0.1 <= slider_bouteilles.value < 0.2:
		label_nbre_bouteilles.text = '1'
		
	elif 0.2 <= slider_bouteilles.value < 0.3:
		label_nbre_bouteilles.text = '2'
		
	elif 0.3 <= slider_bouteilles.value < 0.4:
		label_nbre_bouteilles.text = '3'
		
	elif 0.4 <= slider_bouteilles.value < 0.5:
		label_nbre_bouteilles.text = '4'
		
	elif 0.5 <= slider_bouteilles.value < 0.6:
		label_nbre_bouteilles.text = '5'
		
	elif 0.6 <= slider_bouteilles.value < 0.7:
		label_nbre_bouteilles.text = '6'
		
	elif 0.7 <= slider_bouteilles.value < 0.8:
		label_nbre_bouteilles.text = '7'
		
	elif 0.8 <= slider_bouteilles.value < 0.9:
		label_nbre_bouteilles.text = '8'
		
	elif 0.9 <= slider_bouteilles.value < 1:
		label_nbre_bouteilles.text = '9'
		
	elif slider_bouteilles.value == 1:
		label_nbre_bouteilles.text = '10'
		
	return None
	
	
def slider_petites_canettes(sender):
	"""
	slider_petites_canettes : sender -> None
	slider_petites_canettes(sender) modifie le texte du label label_nbre_petites_canettes en fonction de la valeur retournée par le slider slider_petites_canettes, return None.
	"""
	global slider_petites_canettes
	global label_nbre_petites_canettes
	
	if slider_petites_canettes.value < 0.1:
		label_nbre_petites_canettes.text = ''
		
	elif 0.1 <= slider_petites_canettes.value < 0.2:
		label_nbre_petites_canettes.text = '1'
		
	elif 0.2 <= slider_petites_canettes.value < 0.3:
		label_nbre_petites_canettes.text = '2'
		
	elif 0.3 <= slider_petites_canettes.value < 0.4:
		label_nbre_petites_canettes.text = '3'
		
	elif 0.4 <= slider_petites_canettes.value < 0.5:
		label_nbre_petites_canettes.text = '4'
		
	elif 0.5 <= slider_petites_canettes.value < 0.6:
		label_nbre_petites_canettes.text = '5'
		
	elif 0.6 <= slider_petites_canettes.value < 0.7:
		label_nbre_petites_canettes.text = '6'
		
	elif 0.7 <= slider_petites_canettes.value < 0.8:
		label_nbre_petites_canettes.text = '7'
		
	elif 0.8 <= slider_petites_canettes.value < 0.9:
		label_nbre_petites_canettes.text = '8'
		
	elif 0.9 <= slider_petites_canettes.value < 1:
		label_nbre_petites_canettes.text = '9'
		
	elif slider_petites_canettes.value == 1:
		label_nbre_petites_canettes.text = '10'
		
	return None
	
	
def slider_grandes_canettes(sender):
	"""
	slider_grandes_canettes : sender -> None
	slider_grandes_canettes(sender) modifie le texte du label label_nbre_grandes_canettes en fonction de la valeur retournée par le slider slider_grandes_canettes, return None.
	"""
	global slider_grandes_canettes
	global label_nbre_grandes_canettes
	
	if slider_grandes_canettes.value < 0.1:
		label_nbre_grandes_canettes.text = ''
		
	elif 0.1 <= slider_grandes_canettes.value < 0.2:
		label_nbre_grandes_canettes.text = '1'
		
	elif 0.2 <= slider_grandes_canettes.value < 0.3:
		label_nbre_grandes_canettes.text = '2'
		
	elif 0.3 <= slider_grandes_canettes.value < 0.4:
		label_nbre_grandes_canettes.text = '3'
		
	elif 0.4 <= slider_grandes_canettes.value < 0.5:
		label_nbre_grandes_canettes.text = '4'
		
	elif 0.5 <= slider_grandes_canettes.value < 0.6:
		label_nbre_grandes_canettes.text = '5'
		
	elif 0.6 <= slider_grandes_canettes.value < 0.7:
		label_nbre_grandes_canettes.text = '6'
		
	elif 0.7 <= slider_grandes_canettes.value < 0.8:
		label_nbre_grandes_canettes.text = '7'
		
	elif 0.8 <= slider_grandes_canettes.value < 0.9:
		label_nbre_grandes_canettes.text = '8'
		
	elif 0.9 <= slider_grandes_canettes.value < 1:
		label_nbre_grandes_canettes.text = '9'
		
	elif slider_grandes_canettes.value == 1:
		label_nbre_grandes_canettes.text = '10'
		
	return None
	
	
def button_validation_volumes_bieres(sender):
	"""
	button_validation_volumes_bieres : sender -> None
	button_validation_volumes_bieres(sender) affecte la masse d'alcool ingérée a la variable masse_alcool_totale, ajoute la sous-vue view_boucle_calculatrice, return None.
	"""
	global view_genre
	global view_boucle_calculatrice
	global slider_bouteilles
	global slider_petites_canettes
	global slider_grandes_canettes
	global label_nbre_bouteilles
	global label_nbre_petites_canettes
	global label_nbre_grandes_canettes
	global degre_alcoolique
	global masse_alcool_totale
	
	volume_boisson = 0
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if label_nbre_bouteilles.text != '':
		nbre_bouteilles = int(label_nbre_bouteilles.text)
		volume_boisson += (250 * nbre_bouteilles)
		
	else:
		None
		
	if label_nbre_petites_canettes.text != '':
		nbre_petites_canettes = int(label_nbre_petites_canettes.text)
		volume_boisson += (330 * nbre_petites_canettes)
		
	else:
		None
		
	if label_nbre_grandes_canettes.text != '':
		nbre_grandes_canettes = int(label_nbre_grandes_canettes.text)
		volume_boisson += (500 * nbre_grandes_canettes)
		
	else:
		None
		
	# Remise à 0 de la valeur des sliders et des labels. 
	slider_bouteilles.value = 0.0
	slider_petites_canettes.value = 0.0
	slider_grandes_canettes.value = 0.0
	
	label_nbre_bouteilles.text = ''
	label_nbre_petites_canettes.text = ''
	label_nbre_grandes_canettes.text = ''
	
	masse_alcool_ingeree = ((volume_boisson / 100) * degre_alcoolique) * 0.789
	masse_alcool_totale += masse_alcool_ingeree
	degre_alcoolique = 0
	
	view_genre.add_subview(view_boucle_calculatrice)
	
	return None
	
	
"""
View categories_spiritueux. Affiche 4 boutons, une zone de texte et un slider, le noms et la fonction des boutons changent en fonction de la valeur comprise entre 0 et 1, retournée par le slider. A l'appel de chaque bouton, affichage de  la sous-vue view_volumes_spiritueux, affectation de la valeur du degré alcoolique à la variable globale degre_alcoolique. 
"""

def button_1_categories_spiritueux(sender):
	"""
	button_1_categories_spiritueux : sender -> None
	button_1_categories_spiritueux(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux ou view_gin_calculatrice, return None.
	"""
	global view_genre
	global view_liqueurs_calculatrice
	global view_volumes_spiritueux
	global button_1_categories_spiritueux
	global degre_alcoolique	
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_1_categories_spiritueux.title == 'Gin':
		view_genre.add_subview(view_gin_calculatrice)
		
	elif button_1_categories_spiritueux.title == 'Ricard':
		titre_alcoometrique_Ricard = 45
		degre_alcoolique += titre_alcoometrique_Ricard
		view_genre.add_subview(view_volumes_spiritueux)
		
	return None
	
	
def button_2_categories_spiritueux(sender):
	"""
	button_2_categories_spiritueux : sender -> None
	button_2_categories_spiritueux(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux ou view_liqueurs_calculatrice, return None.
	"""
	global view_genre
	global view_tequila_calculatrice
	global view_volumes_spiritueux
	global button_2_categories_spiritueux
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_2_categories_spiritueux.title == 'Liqueurs':
		view_genre.add_subview(view_liqueurs_calculatrice)
		
	elif button_2_categories_spiritueux.title == 'Tequila':
		titre_alcoometrique_Tequila = 35
		degre_alcoolique += titre_alcoometrique_Tequila
		view_genre.add_subview(view_volumes_spiritueux)
		
	return None
	
	
def button_3_categories_spiritueux(sender):
	"""
	button_3_categories_spiritueux : sender -> None
	button_3_categories_spiritueux(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux ou view_vodka_calculatrice, return None.
	"""
	global view_genre
	global view_vodka_calculatrice
	global view_volumes_spiritueux
	global button_3_categories_spiritueux
	global degre_alcoolique
	
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_3_categories_spiritueux.title == 'Meiguilujiu':
		titre_alcoometrique_Meiguilujiu = 40
		degre_alcoolique += titre_alcoometrique_Meiguilujiu
		view_genre.add_subview(view_volumes_spiritueux)
		
	elif button_3_categories_spiritueux.title == 'Vodka':
		view_genre.add_subview(view_vodka_calculatrice)
		
	return None
	
	
def button_4_categories_spiritueux(sender):
	"""
	button_4_categories_spiritueux : sender -> None
	button_4_categories_spiritueux(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux ou view_rhum_calculatrice, return None.
	"""
	global view_genre
	global view_rhum_calculatrice
	global view_wisky_calculatrice
	global view_volumes_spiritueux
	global button_4_categories_spiritueux
	global label_demi_shot
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_4_categories_spiritueux.title == 'Rhum':
		view_genre.add_subview(view_rhum_calculatrice)
		
	elif button_4_categories_spiritueux.title == 'Whisky':
		titre_alcoometrique_Whisky = 40
		degre_alcoolique += titre_alcoometrique_Whisky
		label_demi_shot.text = 'Baby 2 Cl'
		view_genre.add_subview(view_volumes_spiritueux)
		
	return None
	
	
def slider_categories_spiritueux(sender):
	"""
	slider_categories_spiritueux : sender -> None
	slider_categories_spiritueux(sender) modifie les titres des boutons de la sous-vue view_categories_spiritueux en fonction de la valeur retournée par le slider slider_categories_spiritueux, return None.
	"""
	global button_1_categories_spiritueux
	global button_2_categories_spiritueux
	global button_3_categories_spiritueux
	global button_4_categories_spiritueux
	global slider_categories_spiritueux
	
	if slider_categories_spiritueux.value < 0.5:
		button_1_categories_spiritueux.title = 'Gin'
		button_2_categories_spiritueux.title = 'Liqueurs'
		button_3_categories_spiritueux.title = 'Meiguilujiu'
		button_4_categories_spiritueux.title = 'Rhum'
		
	elif slider_categories_spiritueux.value >= 0.5:
		button_1_categories_spiritueux.title = 'Ricard'
		button_2_categories_spiritueux.title = 'Tequila'
		button_3_categories_spiritueux.title = 'Vodka'
		button_4_categories_spiritueux.title = 'Whisky'
		
	return None
	
	
"""
View Gin. Affiche 4 boutons et une zone de texte. Permet à l'utilisateur de selectionner une marque de gin. Affecte le titre alcoométrique de la boisson selectonnée à la variable degre_alcoolique, chaque bouton ajoute la sous-vue view_volumes_spiritueux.
"""

def button_1_gin_calculatrice(sender):
	"""
	button_1_gin_calculatrice : sender -> None
	button_1_gin_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global degre_alcoolique	
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Bombay_Sapphire = 40
	degre_alcoolique += titre_alcoometrique_Bombay_Sapphire
	
	view_genre.add_subview(view_volumes_spiritueux)
	
	return None
	
	
def button_2_gin_calculatrice(sender):
	"""
	button_2_gin_calculatrice : sender -> None
	button_2_gin_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux	
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Citadelle = 44
	degre_alcoolique += titre_alcoometrique_Citadelle
	
	view_genre.add_subview(view_volumes_spiritueux)
	
	return None
	
	
def button_3_gin_calculatrice(sender):
	"""
	button_3_gin_calculatrice : sender -> None
	button_3_gin_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global degre_alcoolique
		
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Hendricks = 41.4
	degre_alcoolique += titre_alcoometrique_Hendricks
	
	view_genre.add_subview(view_volumes_spiritueux)
	
	return None
	
	
def button_4_gin_calculatrice(sender):
	"""
	button_4_gin_calculatrice : sender -> None
	button_4_gin_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Tanqueray = 47.3
	degre_alcoolique += titre_alcoometrique_Tanqueray
	
	view_genre.add_subview(view_volumes_spiritueux)
	
	return None
	
	
"""
View Liqueurs. Affiche 4 boutons et une zone de texte. Permet à l'utilisateur de selectionner une marque de liqueur. Affecte le titre alcoométrique de la boisson selectonnée à la variable degre_alcoolique, chaque bouton ajoute la sous-vue view_volumes_spiritueux.
"""

def button_1_liqueurs_calculatrice(sender):
	"""
	button_1_liqueurs_calculatrice : sender -> None
	button_1_liqueurs_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_liqueurs_calculatrice
	global button_1_liqueurs_calculatrice
	global slider_liqueurs_calculatrice
	global degre_alcoolique	
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_1_liqueurs_calculatrice.title == 'Chartreuse':
		titre_alcoometrique_Chartreuse = 55
		degre_alcoolique += titre_alcoometrique_Chartreuse
		
	elif button_1_liqueurs_calculatrice.title == 'Get 31':
		titre_alcoometrique_Get31 = 24
		degre_alcoolique += titre_alcoometrique_Get31
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_liqueurs_calculatrice.value = 0
	
	return None
	
	
def button_2_liqueurs_calculatrice(sender):
	"""
	button_2_liqueurs_calculatrice : sender -> None
	button_2_liqueurs_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_liqueurs_calculatrice
	global button_2_liqueurs_calculatrice
	global slider_liqueurs_calculatrice
	global degre_alcoolique	
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_2_liqueurs_calculatrice.title == 'Cointreau':
		titre_alcoometrique_Cointreau = 40
		degre_alcoolique += titre_alcoometrique_Cointreau
		
	elif button_2_liqueurs_calculatrice.title == 'Jägermeister':
		titre_alcoometrique_Jagermeister = 35
		degre_alcoolique += titre_alcoometrique_Jagermeister
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_liqueurs_calculatrice.value = 0
	
	return None
	
	
def button_3_liqueurs_calculatrice(sender):
	"""
	button_3_liqueurs_calculatrice : sender -> None
	button_3_liqueurs_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_liqueurs_calculatrice
	global button_3_liqueurs_calculatrice
	global slider_liqueurs_calculatrice
	global degre_alcoolique		
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_3_liqueurs_calculatrice.title == 'Génépi':
		titre_alcoometrique_Genepi = 40
		degre_alcoolique += titre_alcoometrique_Genepi
		
	elif button_3_liqueurs_calculatrice.title == 'Martini':
		titre_alcoometrique_Martini = 14.4
		degre_alcoolique += titre_alcoometrique_Martini
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_liqueurs_calculatrice.value = 0
	
	return None
	
	
def button_4_liqueurs_calculatrice(sender):
	"""
	button_4_liqueurs_calculatrice : sender -> None
	button_4_liqueurs_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_liqueurs_calculatrice
	global button_4_liqueurs_calculatrice
	global slider_liqueurs_calculatrice
	global degre_alcoolique
		
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_4_liqueurs_calculatrice.title == 'Get 27':
		titre_alcoometrique_Get27 = 21
		degre_alcoolique += titre_alcoometrique_Get27
		
	elif button_4_liqueurs_calculatrice.title == 'Suze':
		titre_alcoometrique_Suze = 15
		degre_alcoolique += titre_alcoometrique_Suze
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_liqueurs_calculatrice.value = 0
	
	return None
	
	
def slider_liqueurs_calculatrice(sender):
	"""
	slider_liqueurs_calculatrice : sender -> None
	slider_liqueurs_calculatrice (sender) modifie les titres des boutons de la sous-vue view_categories_spiritueux en fonction de la valeur retournée par le slider slider_liqueurs_calculatrice, return None.
	"""
	global button_1_liqueurs_calculatrice
	global button_2_liqueurs_calculatrice
	global button_3_liqueurs_calculatrice
	global button_4_liqueurs_calculatrice
	global slider_liqueurs_calculatrice
	
	if slider_liqueurs_calculatrice.value < 0.50:
		button_1_liqueurs_calculatrice.title = 'Chartreuse'
		button_2_liqueurs_calculatrice.title = 'Cointreau'
		button_3_liqueurs_calculatrice.title = 'Génépi'
		button_4_liqueurs_calculatrice.title = 'Get 27'
		
	elif slider_liqueurs_calculatrice.value >= 0.50:
		button_1_liqueurs_calculatrice.title = 'Get 31'
		button_2_liqueurs_calculatrice.title = 'Jägermeister'
		button_3_liqueurs_calculatrice.title = 'Martini'
		button_4_liqueurs_calculatrice.title = 'Suze'
		
	return None
	
	
"""
View Rhum. Affiche 4 boutons et une zone de texte. Permet à l'utilisateur de selectionner une marque de rhum. Affecte le titre alcoométrique de la boisson selectonnée à la variable degre_alcoolique, chaque bouton ajoute la sous-vue view_volumes_spiritueux.
"""

def button_1_rhum_calculatrice(sender):
	"""
	button_1_rhum_calculatrice : sender -> None
	button_1_rhum_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global button_1_rhum_calculatrice
	global slider_rhum_calculatrice
	global degre_alcoolique		
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_1_rhum_calculatrice.title == 'Bacardi':
		titre_alcoometrique_Bacardi = 37.5
		degre_alcoolique += titre_alcoometrique_Bacardi
		
	elif button_1_rhum_calculatrice.title == 'Dillon':
		titre_alcoometrique_Dillon = 55
		degre_alcoolique += titre_alcoometrique_Dillon
		
	elif button_1_rhum_calculatrice.title == 'Maison Mauny':
		titre_alcoometrique_Maison_Mauny = 5.0
		degre_alcoolique += titre_alcoometrique_Maison_Mauny
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_rhum_calculatrice.value = 0.0
	
	return None
	
	
def button_2_rhum_calculatrice(sender):
	"""
	button_2_rhum_calculatrice : sender -> None
	button_2_rhum_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global button_2_rhum_calculatrice
	global slider_rhum_calculatrice
	global degre_alcoolique		
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_2_rhum_calculatrice.title == 'Captain Morgan':
		titre_alcoometrique_Captain_Morgan = 35
		degre_alcoolique += titre_alcoometrique_Captain_Morgan
		
	elif button_2_rhum_calculatrice.title == 'Diplomatico':
		titre_alcoometrique_Diplomatico = 40
		degre_alcoolique += titre_alcoometrique_Diplomatico
		
	elif button_2_rhum_calculatrice.title == 'Old Nick Blanc':
		titre_alcoometrique_Old_Nick_Blanc = 40
		degre_alcoolique += titre_alcoometrique_Old_Nick_Blanc
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_rhum_calculatrice.value = 0.0
	
	return None
	
	
def button_3_rhum_calculatrice(sender):
	"""
	button_3_rhum_calculatrice : sender -> None
	button_3_rhum_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global button_3_rhum_calculatrice
	global slider_rhum_calculatrice
	global degre_alcoolique		
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_3_rhum_calculatrice.title == 'Charrette':
		titre_alcoometrique_Charrette = 49
		degre_alcoolique += titre_alcoometrique_Charrette
		
	elif button_3_rhum_calculatrice.title == 'Havana Club':
		titre_alcoometrique_Havana_club = 40
		degre_alcoolique += titre_alcoometrique_Havana_club
		
	elif button_3_rhum_calculatrice.title == 'Saint James':
		titre_alcoometrique_Saint_James = 40
		degre_alcoolique += titre_alcoometrique_Saint_James
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_rhum_calculatrice.value = 0.0
	
	return None
	
	
def button_4_rhum_calculatrice(sender):
	"""
	button_4_rhum_calculatrice : sender -> None
	button_4_rhum_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global button_4_rhum_calculatrice
	global slider_rhum_calculatrice
	global degre_alcoolique		
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_4_rhum_calculatrice.title == 'Crean':
		titre_alcoometrique_Crean = 40
		degre_alcoolique += titre_alcoometrique_Crean
		
	elif button_4_rhum_calculatrice.title == 'HSE':
		titre_alcoometrique_Hse = 55
		degre_alcoolique += titre_alcoometrique_Hse
		
	elif button_4_rhum_calculatrice.title == 'Trois Rivières':
		titre_alcoometrique_Trois_rivieres = 50
		degre_alcoolique += titre_alcoometrique_Trois_rivieres
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_rhum_calculatrice.value = 0.0
	
	return None

		
def slider_rhum_calculatrice(sender):
	"""
	slider_rhum_calculatrice : sender -> None
	slider_rhum_calculatrice(sender) modifie les titres des boutons de la sous-vue view_rhum_calculatrice en fonction de la valeur retournée par le slider slider_rhum_calculatrice, return None.
	"""
	global button_1_rhum_calculatrice
	global button_2_rhum_calculatrice
	global button_3_rhum_calculatrice
	global button_4_rhum_calculatrice
	global slider_rhum_calculatrice
	
	
	if slider_rhum_calculatrice.value < 0.333:
		button_1_rhum_calculatrice.title = 'Bacardi'
		button_2_rhum_calculatrice.title = 'Captain Morgan'
		button_3_rhum_calculatrice.title = 'Charrette'
		button_4_rhum_calculatrice.title = 'Crean'
		
	elif 0.333 <= slider_rhum_calculatrice.value < 0.666:
		button_1_rhum_calculatrice.title = 'Dillon'
		button_2_rhum_calculatrice.title = 'Diplomatico'
		button_3_rhum_calculatrice.title = 'Havana Club'
		button_4_rhum_calculatrice.title = 'HSE'
		
	elif 0.666 <= slider_rhum_calculatrice.value:
		button_1_rhum_calculatrice.title = 'Maison Mauny'
		button_2_rhum_calculatrice.title = 'Old Nick Blanc'
		button_3_rhum_calculatrice.title = 'Saint James'
		button_4_rhum_calculatrice.title = 'Trois Rivières'
		
	return None
	
	
"""
View Vodka. Affiche 4 boutons et une zone de texte. Permet à l'utilisateur de selectionner une marque de vodka. Affecte le titre alcoométrique de la boisson selectonnée à la variable degre_alcoolique, chaque bouton ajoute la sous-vue view_volumes_spiritueux.
"""

def button_1_vodka_calculatrice(sender):
	"""
	button_1_vodka_calculatrice : sender -> None
	button_1_vodka_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None.
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_vodka_calculatrice
	global button_1_vodka_calculatrice
	global slider_vodka_calculatrice
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_1_vodka_calculatrice.title == 'Absolut':
		titre_alcoometrique_Absolut = 40
		degre_alcoolique += titre_alcoometrique_Absolut
		
	elif button_1_vodka_calculatrice.title == 'Grey Goose':
		titre_alcoometrique_Grey_Goose = 40
		degre_alcoolique += titre_alcoometrique_Grey_Goose
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_vodka_calculatrice.value = 0
	
	return None
	
	
def button_2_vodka_calculatrice(sender):
	"""
	button_2_vodka_calculatrice : sender -> None
	button_2_vodka_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_vodka_calculatrice
	global button_2_vodka_calculatrice
	global slider_vodka_calculatrice
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_2_vodka_calculatrice.title == 'Belvedere':
		titre_alcoometrique_Belvedere = 40
		degre_alcoolique += titre_alcoometrique_Belvedere
		
	elif button_2_vodka_calculatrice.title == 'Poliakov':
		titre_alcoometrique_Poliakov = 37.5
		degre_alcoolique += titre_alcoometrique_Poliakov
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_vodka_calculatrice.value = 0
	
	return None
	
	
def button_3_vodka_calculatrice(sender):
	"""
	button_3_vodka_calculatrice : sender -> None
	button_3_vodka_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_vodka_calculatrice
	global button_3_vodka_calculatrice
	global slider_vodka_calculatrice
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_3_vodka_calculatrice.title == 'Ciroc':
		titre_alcoometrique_Ciroc = 40
		degre_alcoolique += titre_alcoometrique_Ciroc
		
	elif button_3_vodka_calculatrice.title == 'Sobieski':
		titre_alcoometrique_Sobieski = 37.5
		degre_alcoolique += titre_alcoometrique_Sobieski
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_vodka_calculatrice.value = 0
	
	return None
	
	
def button_4_vodka_calculatrice(sender):
	"""
	button_4_vodka_calculatrice : sender -> None
	button_4_vodka_calculatrice(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_spiritueux, return None
	"""
	global view_genre
	global view_volumes_spiritueux
	global view_vodka_calculatrice
	global button_4_vodka_calculatrice
	global slider_vodka_calculatrice
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if button_4_vodka_calculatrice.title == 'Eristoff':
		titre_alcoometrique_Eristoff = 37.5
		degre_alcoolique += titre_alcoometrique_Eristoff
		
	elif button_4_vodka_calculatrice.title == 'Żubrówka':
		titre_alcoometrique_Zubrowka = 37.5
		degre_alcoolique += titre_alcoometrique_Zubrowka
		
	view_genre.add_subview(view_volumes_spiritueux)
	slider_vodka_calculatrice.value = 0
	
	return None
	
	
def slider_vodka_calculatrice(sender):
	"""
	slider_vodka_calculatrice : sender -> None
	slider_vodka_calculatrice (sender) modifie les titres des boutons de la sous-vue view_vodka_calculatrice en fonction de la valeur retournée par le slider slider_vodka_calculatrice, return None.
	"""
	global button_1_vodka_calculatrice
	global button_2_vodka_calculatrice
	global button_3_vodka_calculatrice
	global button_4_vodka_calculatrice
	global slider_vodka_calculatrice
	
	if slider_vodka_calculatrice.value < 0.5:
		button_1_vodka_calculatrice.title = 'Absolut'
		button_2_vodka_calculatrice.title = 'Belvedere'
		button_3_vodka_calculatrice.title = 'Ciroc'
		button_4_vodka_calculatrice.title = 'Eristoff'
		
	elif slider_vodka_calculatrice.value >= 0.5:
		button_1_vodka_calculatrice.title = 'Grey Goose'
		button_2_vodka_calculatrice.title = 'Poliakov'
		button_3_vodka_calculatrice.title = 'Sobieski'
		button_4_vodka_calculatrice.title = 'Żubrówka'
		
	return None
	
	
"""
View Volumes_spiritueux. Permet à l'utilisateur de selectionner le volume de boisson consommée, ainsi que le nombre de doses. ajoute la sous-vue view_boucle_calculatrice et affecte la valeur de la quantité d'alcool ingérée à la variable globale masse_alcool_totale.
"""

def slider_demi_shot(sender):
	"""
	slider_shot : sender -> None
	slider_shot(sender) modifie le texte du label label_nbre_demi_shot en fonction de la valeur retournée par le slider slider_demi_shot, return None.
	"""	
	global slider_demi_shot
	global label_nbre_demi_shot
	
	if slider_demi_shot.value < 0.1:
		label_nbre_demi_shot.text = ''
		
	elif 0.1 <= slider_demi_shot.value < 0.2:
		label_nbre_demi_shot.text = '1'
		
	elif 0.2 <= slider_demi_shot.value < 0.3:
		label_nbre_demi_shot.text = '2'
		
	elif 0.3 <= slider_demi_shot.value < 0.4:
		label_nbre_demi_shot.text = '3'
		
	elif 0.4 <= slider_demi_shot.value < 0.5:
		label_nbre_demi_shot.text = '4'
		
	elif 0.5 <= slider_demi_shot.value < 0.6:
		label_nbre_demi_shot.text = '5'
		
	elif 0.6 <= slider_demi_shot.value < 0.7:
		label_nbre_demi_shot.text = '6'
		
	elif 0.7 <= slider_demi_shot.value < 0.8:
		label_nbre_demi_shot.text = '7'
		
	elif 0.8 <= slider_demi_shot.value < 0.9:
		label_nbre_demi_shot.text = '8'
		
	elif 0.9 <= slider_demi_shot.value < 1:
		label_nbre_demi_shot.text = '9'
		
	elif slider_demi_shot.value == 1:
		label_nbre_demi_shot.text = '10'
		
	return None
	
	
def slider_shot(sender):
	"""
	slider_shot : sender -> None
	slider_shot(sender) modifie le texte du label label_nbre_shot en fonction de la valeur retournée par le slider slider_shot, return None.
	"""
	global slider_shot
	global label_nbre_shot
	
	if slider_shot.value < 0.1:
		label_nbre_shot.text = ''
		
	elif 0.1 <= slider_shot.value < 0.2:
		label_nbre_shot.text = '1'
		
	elif 0.2 <= slider_shot.value < 0.3:
		label_nbre_shot.text = '2'
		
	elif 0.3 <= slider_shot.value < 0.4:
		label_nbre_shot.text = '3'
		
	elif 0.4 <= slider_shot.value < 0.5:
		label_nbre_shot.text = '4'
		
	elif 0.5 <= slider_shot.value < 0.6:
		label_nbre_shot.text = '5'
		
	elif 0.6 <= slider_shot.value < 0.7:
		label_nbre_shot.text = '6'
		
	elif 0.7 <= slider_shot.value < 0.8:
		label_nbre_shot.text = '7'
		
	elif 0.8 <= slider_shot.value < 0.9:
		label_nbre_shot.text = '8'
		
	elif 0.9 <= slider_shot.value < 1:
		label_nbre_shot.text = '9'
		
	elif slider_shot.value == 1:
		label_nbre_shot.text = '10'
		
	return None
	
	
def slider_cocktail(sender):
	"""
	slider_cocktail : sender -> None
	slider_cocktail(sender) modifie le texte du label label_nbre_grandes_canettes en fonction de la valeur retournée par le slider slider_grandes_canettes, return None.
	"""
	global slider_cocktail
	global label_nbre_cocktail
	
	if slider_cocktail.value < 0.1:
		label_nbre_cocktail.text = ''
		
	elif 0.1 <= slider_cocktail.value < 0.2:
		label_nbre_cocktail.text = '1'
		
	elif 0.2 <= slider_cocktail.value < 0.3:
		label_nbre_cocktail.text = '2'
		
	elif 0.3 <= slider_cocktail.value < 0.4:
		label_nbre_cocktail.text = '3'
		
	elif 0.4 <= slider_cocktail.value < 0.5:
		label_nbre_cocktail.text = '4'
		
	elif 0.5 <= slider_cocktail.value < 0.6:
		label_nbre_cocktail.text = '5'
		
	elif 0.6 <= slider_cocktail.value < 0.7:
		label_nbre_cocktail.text = '6'
		
	elif 0.7 <= slider_cocktail.value < 0.8:
		label_nbre_cocktail.text = '7'
		
	elif 0.8 <= slider_cocktail.value < 0.9:
		label_nbre_cocktail.text = '8'
		
	elif 0.9 <= slider_cocktail.value < 1:
		label_nbre_cocktail.text = '9'
		
	elif slider_cocktail.value == 1:
		label_nbre_cocktail.text = '10'
		
	return None
	
	
def button_validation_volumes_spiritueux(sender):
	"""
	button_validation_volumes_spiritueux : sender -> None
	button_validation_volumes_spiritueux(sender) ajoute la masse d'alcool ingérée a la variable masse_alcool_totale, ajoute la sous-vue view_boucle_calculatrice, return None.
	"""
	global view_genre
	global view_boucle_calculatrice
	global slider_demi_shot
	global slider_shot
	global slider_cocktail
	global label_nbre_demi_shot
	global label_nbre_shot
	global label_nbre_cocktail
	global degre_alcoolique
	global masse_alcool_totale
		
	volume_boisson = 0
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if label_nbre_demi_shot.text != '':
		nbre_demi_shot = int(label_nbre_demi_shot.text)
		volume_boisson += (20 * nbre_demi_shot)
		
	else:
		None
		
	if label_nbre_shot.text != '':
		nbre_shot = int(label_nbre_shot.text)
		volume_boisson += (40 * nbre_shot)
		
	else:
		None
		
	if label_nbre_cocktail.text != '':
		nbre_cocktail = int(label_nbre_cocktail.text)
		volume_boisson += (70 * nbre_cocktail)
		
	else:
		None
		
	# Remise à 0 de la valeur des sliders et des labels.
	slider_demi_shot.value = 0.0
	slider_shot.value = 0.0
	slider_cocktail.value = 0.0
	
	label_nbre_demi_shot.text = ''
	label_nbre_shot.text = ''
	label_nbre_cocktail.text = ''
	
	masse_alcool_ingeree = ((volume_boisson / 100) * degre_alcoolique) * 0.789
	masse_alcool_totale += masse_alcool_ingeree
	degre_alcoolique = 0
	
	view_genre.add_subview(view_boucle_calculatrice)
	
	return None
	
	
"""
View categories_vins. Affiche 4 boutons, une zone de texte. A l'appel de chaque bouton, affichage de  la sous-vue view_volumes_vins, affectation de la valeur du degré alcoolique à la variable globale degre_alcoolique.
"""

def button_1_categories_vins(sender):
	"""
	button_1_categories_vins : sender -> None
	button_1_categories_vins(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_vins, return None.
	"""
	global view_genre
	global view_volumes_vins
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Blanc = 12
	degre_alcoolique += titre_alcoometrique_Blanc
	
	view_genre.add_subview(view_volumes_vins)
	
	return None
	
	
def button_2_categories_vins(sender):
	"""
	button_2_categories_vins : sender -> None
	button_2_categories_vins(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_vins, return None.
	"""
	global view_genre
	global view_volumes_vins
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Champagne = 12
	degre_alcoolique += titre_alcoometrique_Champagne
	
	view_genre.add_subview(view_volumes_vins)
	
	return None
	
	
def button_3_categories_vins(sender):
	"""
	button_3_categories_vins : sender -> None
	button_3_categories_vins(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_vins, return None.
	"""
	global view_genre
	global view_volumes_vins
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Rose = 12
	degre_alcoolique += titre_alcoometrique_Rose
	
	view_genre.add_subview(view_volumes_vins)
	
	return None
	
	
def button_4_categories_vins(sender):
	"""
	button_1_categories_vins : sender -> None
	button_1_categories_vins(sender) affecte la valeur du titre alcoometrique de la boisson selectionnée dans la liste degre_alcoolique, ajoute la sous_vue view_volumes_vins, return None.
	"""
	global view_genre
	global view_volumes_vins
	global degre_alcoolique
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	titre_alcoometrique_Rouge = 12
	degre_alcoolique += titre_alcoometrique_Rouge
	
	view_genre.add_subview(view_volumes_vins)
	
	return None
	
	
"""
View Volumes_vins. Permet à l'utilisateur de selectionner le volume de boisson consommée, ainsi que le nombre de doses. ajoute la sous-vue view_boucle_calculatrice et affecte la valeur de la quantité d'alcool ingérée à la variable globale masse_alcool_totale.
"""

def slider_ballon(sender):
	"""
	slider_ballon : sender -> None
	slider_ballon(sender) modifie le texte du label label_nbre_ballon en fonction de la valeur retournée par le slider slider_ballon, return None.
	"""
	
	global slider_ballon
	global label_nbre_ballon
	
	if slider_ballon.value < 0.1:
		label_nbre_ballon.text = ''
		
	elif 0.1 <= slider_ballon.value < 0.2:
		label_nbre_ballon.text = '1'
		
	elif 0.2 <= slider_ballon.value < 0.3:
		label_nbre_ballon.text = '2'
		
	elif 0.3 <= slider_ballon.value < 0.4:
		label_nbre_ballon.text = '3'
		
	elif 0.4 <= slider_ballon.value < 0.5:
		label_nbre_ballon.text = '4'
		
	elif 0.5 <= slider_ballon.value < 0.6:
		label_nbre_ballon.text = '5'
		
	elif 0.6 <= slider_ballon.value < 0.7:
		label_nbre_ballon.text = '6'
		
	elif 0.7 <= slider_ballon.value < 0.8:
		label_nbre_ballon.text = '7'
		
	elif 0.8 <= slider_ballon.value < 0.9:
		label_nbre_ballon.text = '8'
		
	elif 0.9 <= slider_ballon.value < 1:
		label_nbre_ballon.text = '9'
		
	elif slider_ballon.value == 1:
		label_nbre_ballon.text = '10'
		
	return None
	
	
def slider_verre(sender):
	"""
	slider_verre : sender -> None
	slider_verre(sender) modifie le texte du label label_nbre_verre en fonction de la valeur retournée par le slider slider_verre, return None.
	"""
	global slider_verre
	global label_nbre_verre
	
	if slider_verre.value < 0.1:
		label_nbre_verre.text = ''
		
	elif 0.1 <= slider_verre.value < 0.2:
		label_nbre_verre.text = '1'
		
	elif 0.2 <= slider_verre.value < 0.3:
		label_nbre_verre.text = '2'
		
	elif 0.3 <= slider_verre.value < 0.4:
		label_nbre_verre.text = '3'
		
	elif 0.4 <= slider_verre.value < 0.5:
		label_nbre_verre.text = '4'
		
	elif 0.5 <= slider_verre.value < 0.6:
		label_nbre_verre.text = '5'
		
	elif 0.6 <= slider_verre.value < 0.7:
		label_nbre_verre.text = '6'
		
	elif 0.7 <= slider_verre.value < 0.8:
		label_nbre_verre.text = '7'
		
	elif 0.8 <= slider_verre.value < 0.9:
		label_nbre_verre.text = '8'
		
	elif 0.9 <= slider_verre.value < 1:
		label_nbre_verre.text = '9'
		
	elif slider_verre.value == 1:
		label_nbre_verre.text = '10'
		
	return None
	
	
def slider_cup(sender):
	"""
	slider_cup : sender -> None
	slider_cup(sender) modifie le texte du label label_nbre_cup en fonction de la valeur retournée par le slider slider_cup, return None.
	"""
	global slider_cup
	global label_nbre_cup
	
	if slider_cup.value < 0.1:
		label_nbre_cup.text = ''
		
	elif 0.1 <= slider_cup.value < 0.2:
		label_nbre_cup.text = '1'
		
	elif 0.2 <= slider_cup.value < 0.3:
		label_nbre_cup.text = '2'
		
	elif 0.3 <= slider_cup.value < 0.4:
		label_nbre_cup.text = '3'
		
	elif 0.4 <= slider_cup.value < 0.5:
		label_nbre_cup.text = '4'
		
	elif 0.5 <= slider_cup.value < 0.6:
		label_nbre_cup.text = '5'
		
	elif 0.6 <= slider_cup.value < 0.7:
		label_nbre_cup.text = '6'
		
	elif 0.7 <= slider_cup.value < 0.8:
		label_nbre_cup.text = '7'
		
	elif 0.8 <= slider_cup.value < 0.9:
		label_nbre_cup.text = '8'
		
	elif 0.9 <= slider_cup.value < 1:
		label_nbre_cup.text = '9'
		
	elif slider_cup.value == 1:
		label_nbre_cup.text = '10'
		
	return None
	
def button_validation_volumes_vins(sender):
	"""
	button_validation_volumes_vins : sender -> None
	button_validation_volumes_vins(sender) affecte la valeur de la masse d'alcool ingérée a la variable masse_alcool_totale, ajoute la sous-vue view_boucle_calculatrice, return None.
	"""
	global view_genre
	global view_boucle_calculatrice
	global slider_ballon
	global slider_verre
	global slider_cup
	global label_nbre_ballon
	global label_nbre_verre
	global label_nbre_cup
	global degre_alcoolique
	global masse_alcool_totale		
	
	volume_boisson = 0
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	if label_nbre_ballon.text != '':
		nbre_ballon = int(label_nbre_ballon.text)
		volume_boisson += (125 * nbre_ballon)
		
	else:
		None
		
	if label_nbre_verre.text != '':
		nbre_verre = int(label_nbre_verre.text)
		volume_boisson += (250 * nbre_verre)
		
	else:
		None
		
	if label_nbre_cup.text != '':
		nbre_cup = int(label_nbre_cup.text)
		volume_boisson += (330 * nbre_cup)
		
	else:
		None
	
	# Remise à 0 de la valeur des sliders et des labels.
	slider_ballon.value = 0.0
	slider_verre.value = 0.0
	slider_cup.value = 0.0
	
	label_nbre_ballon.text = ''
	label_nbre_verre.text = ''
	label_nbre_cup.text = ''
	
	masse_alcool_ingeree = ((volume_boisson / 100) * degre_alcoolique) * 0.789
	masse_alcool_totale += masse_alcool_ingeree
	degre_alcoolique = 0
	
	view_genre.add_subview(view_boucle_calculatrice)
	
	return None
	
	
"""
View Boucle_calculatrice. Affiche une zone de texte et 2 boutons. L'utilisateur à la choix entre rentrer une nouvelle consommation (ajouter la sous-vue view_classes), et connaitre son taux d'alcoolémie (ajouter la sous-vue view_resultat_calculatrice)
"""

def button_oui_boucle_calculatrice(sender):
	"""
	button_oui_boucle_calculatrice : sender -> None
	button_oui_boucle_calculatrice(sender) ajoute la sous-vue view_classes.
	"""
	global view_genre
	global view_classes
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_genre.add_subview(view_classes)
	
	return None
	
	
def button_non_boucle_calculatrice(sender):
	"""
	button_non_boucle_calculatrice : sender -> None
	button_non_boucle_calculatrice(sender) apelle la fonction traitement_calculatrice, modifie le texte du label label3_resultat_calculatrice, ajoute la sous-vue view_resultat_calculatrice, return None.
	"""
	global view_genre
	global view_resultat_calculatrice
	global button_uber_calculatrice
	global label3_resultat_calculatrice
	global label7_resultat_calculatrice
	global masse_alcool_totale
	global compteur_boucles_calculatrice
	global coefficient_de_diffusion_k
	
	sound.play_effect('ApplePay sound effect.m4a')
	
	taux_alcoolemie = traitement_calculatrice()
	label3_resultat_calculatrice.text = '{}'.format(round(taux_alcoolemie, 2))
	
	if coefficient_de_diffusion_k == 0.6:
		nbre_heures_avant_taux_alcoolemie_nul = taux_alcoolemie / 0.10
		
	else:
		nbre_heures_avant_taux_alcoolemie_nul = taux_alcoolemie / 0.15
		
	label7_resultat_calculatrice.text = '{}'.format(int(nbre_heures_avant_taux_alcoolemie_nul))
	
	if taux_alcoolemie >= 0.5:
		button_uber_calculatrice.image = ui.Image('Uber.PNG')
		button_uber_calculatrice.title = 'Uber'
	
	else:
		None
		
	view_genre.add_subview(view_resultat_calculatrice)
	
	return None
	
	
def traitement_calculatrice():
	"""
	traitement_calculatrice : None -> Float
	traitement_calculatrice() réalise le calcul du taux d'alcoolemie, return Int.
	"""
	global masse_alcool_totale
	global poids_utilisateur
	global coefficient_de_diffusion_k
	
	taux_alcoolemie = (masse_alcool_totale) / (poids_utilisateur * coefficient_de_diffusion_k)
	
	return taux_alcoolemie
	
	
"""
View Resultat_calculatrice. Affiche 2 boutons, un bouton Uber et un bouton home. le bouton Uber permet de lancer l'application Uber Cab, le button home permet de retourner à la premiere page (retire la sous-vue view_genre).
"""

def button_uber_calculatrice(sender):
	"""
	button_uber_calculatrice : sender -> None
	button_uber_calculatrice(sender) ajoute la sou-vue view_uber_calculatrice, return None.
	"""
	global view_genre
	global view_uber_calculatrice
	
	if button_uber_calculatrice.title == 'Uber':
		webbrowser.open('uber://')
		
	else:
		None
		
	return None
	
	
def button_home_resultat_calculatrice(sender):
	"""
	button_home_resultat_calculatrice : sender -> None
	button_home_resultat_calculatrice(sender) retire la sous-vue view_genre, return None.
	"""
	global view_genre
	global view_menu_principal
	
	sound.play_effect('ApplePay sound effect.m4a')
	view_menu_principal.remove_subview(view_genre)
	
	return None
	
	
"""
View Preparation generateur de calcul. Affiche les consignes du generateur de calcul et 1 bouton. Ajoute la sous-vue generateur_de_calcul. Affecte à la variable globale temps_demarrage_generateur_de_calcul, le temps au moment de l'appel.
"""

def button_1_preparation_generateur_de_calcul(sender):
	"""
	button_1_preparation_generateur_de_calcul : sender -> None
	button_1_preparation_generateur_de_calcul(sender) ajoute la sous-vue generateur_de_calcul, affecte à la variable temps_demarrage_generateur_de_calcul, le temps au moment de l'appel.
	"""
	global view_preparation_generateur_de_calcul
	global generateur_de_calcul
	global temps_demarrage_generateur_de_calcul
	
	
	speech.say('Allons y', 'fr-FR') # Réalise la dictée du message en français.
	view_preparation_generateur_de_calcul.add_subview(generateur_de_calcul)
	
	return None
	
	
"""
View generateur_de_calcul. Jeu Generateur de calcul, genere des calculs aléatoires, affiche 14 boutons et 1 zone de texte. le jeu est chronométré et le minuteur s'arrete au bout de 10 calculs. Avant le lancement de l'execution, les chiffres de 1 à 9 émettent un son de piano, le bouton principal, à la capacité d´être dicté par Siri.
"""

# Partition - In The End - Linkin Park = 2448666682
# Partition - Numb  - Linkin Park = 131579131793

def button_principal_generateur_de_calcul(sender):
	"""
	button_principal_generateur_de_calcul : sender -> None
	button_principal_generateur_de_calcul(sender) modifie le titre du bouton button_principal_generateur_de_calcul, en fonction des différentes valeurs en indice 0,1,2 de la liste calculs_aleatoires, modifie l'action du button, qui appelle alors la fonction button_principal_generateur_de_calcul_v2, return None. 
	"""
	global calculs_aleatoires
	global temps_demarrage_generateur_de_calcul
	x = calculs_aleatoires[0]
	y = calculs_aleatoires[1]
	signe_calcul_aleatoire = calculs_aleatoires[2]
	
	temps_demarrage_generateur_de_calcul = time.time()
	
	sender.title = '{} {} {} '.format(x, signe_calcul_aleatoire, y)
	sender.action = button_principal_generateur_de_calcul_v2
	
	return None
	
	
def button_principal_generateur_de_calcul_v2(sender):
	"""
	button_principal_generateur_de_calcul_v2 : sender -> None
	button_principal_generateur_de_calcul_v2(sender) dicte le titre du bouton button_principal_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global calculs_aleatoires
	global compteur
	x = calculs_aleatoires[0]
	y = calculs_aleatoires[1]
	
	if calculs_aleatoires[2] == '-':
		speech.say('{} moins {}'.format(x,y) , 'fr-FR') # Réalise la dictée du titre du bouton button_principal_generateur_de_calcul.
		
	else:
		speech.say(sender.title, 'fr-FR')
		
	return None
		
	
def button_1_generateur_de_calcul(sender):
	"""
	button_1_generateur_de_calcul : sender -> None
	button_1_generateur_de_calcul(sender) ajoute la chaine de caractères '1' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
		
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '1'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note Nb1.m4a')
		
	return None
	
	
def button_2_generateur_de_calcul(sender):
	"""
	button_2_generateur_de_calcul : sender -> None
	button_2_generateur_de_calcul(sender) ajoute la chaine de caractères '2' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '2'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note 1.m4a')
		
	return None
	
	
def button_3_generateur_de_calcul(sender):
	"""
	button_3_generateur_de_calcul : sender -> None
	button_3_generateur_de_calcul(sender) ajoute la chaine de caractères '3' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '3'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note Nb2.m4a')
		
	return None
	
	
def button_4_generateur_de_calcul(sender):
	"""
	button_4_generateur_de_calcul : sender -> None
	button_4_generateur_de_calcul(sender) ajoute la chaine de caractères '4' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul	
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '4'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note 2.m4a')
		
	return None
	
	
def button_5_generateur_de_calcul(sender):
	"""
	button_5_generateur_de_calcul : sender -> None
	button_5_generateur_de_calcul(sender) ajoute la chaine de caractères '5' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '5'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note Nb3.m4a')
		
	return None
	
	
def button_6_generateur_de_calcul(sender):
	"""
	button_6_generateur_de_calcul : sender -> None
	button_6_generateur_de_calcul(sender) ajoute la chaine de caractères '6' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '6'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note 4.m4a')
		
	return None
	
	
def button_7_generateur_de_calcul(sender):
	"""
	button_7_generateur_de_calcul : sender -> None
	button_7_generateur_de_calcul(sender) ajoute la chaine de caractères '7' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul	
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '7'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note Nb4.m4a')
		
	return None
	
	
def button_8_generateur_de_calcul(sender):
	"""
	button_8_generateur_de_calcul : sender -> None
	button_8_generateur_de_calcul(sender) ajoute la chaine de caractères '8' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '8'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note 3.m4a')
		
	return None
	
	
def button_9_generateur_de_calcul(sender):
	"""
	button_9_generateur_de_calcul : sender -> None
	button_9_generateur_de_calcul(sender) ajoute la chaine de caractères '9' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '9'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		sound.play_effect('Note Nb5.m4a')
		
	return None
	
	
def button_0_generateur_de_calcul(sender):
	"""
	button_0_generateur_de_calcul : sender -> None
	button_0_generateur_de_calcul(sender) ajoute la chaine de caractères '0' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) < 3:
			sound.play_effect('ui:mouseclick1')
			valeur = '0'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
			
		else:
			sound.play_effect('ui:mouseclick1')
			
	else:
		None
		
	return None
	
	
def button_negatif_generateur_de_calcul(sender):
	"""
	button_negatif_generateur_de_calcul : sender -> None
	button_negatif_generateur_de_calcul(sender) ajoute la chaine de caractères '-' au Label resultat_generateur_de_calcul et à la liste liste_resultat_generateur_de_calcul, return None.
	"""
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul	
	
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
		if len(liste_resultat_generateur_de_calcul) == 0:
			sound.play_effect('ui:mouseclick1')
			valeur = '-'
			liste_resultat_generateur_de_calcul.append(valeur)
			text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
			resultat_generateur_de_calcul.text = text_generateur_de_calcul
		else:
			None
	
	else:
		None
		
	return None
	
	
def button_delete_generateur_de_calcul(sender):
	"""
	button_delete_generateur_de_calcul : sender -> None
	button_delete_generateur_de_calcul(sender) retire le dernier élément du Label resultat_generateur_de_calcul, return None.
	"""
	global liste_resultat_generateur_de_calcul
	global text_resultat_generateur_de_calcul
	sound.play_effect('ui:rollover2')
	len_liste_resultat_generateur_de_calcul = len(liste_resultat_generateur_de_calcul)
	
	# Algorithme de gestion des erreurs.
	if len_liste_resultat_generateur_de_calcul != 0:
		del liste_resultat_generateur_de_calcul[len_liste_resultat_generateur_de_calcul - 1]
		text_generateur_de_calcul = ''.join(liste_resultat_generateur_de_calcul)
		resultat_generateur_de_calcul.text = text_generateur_de_calcul
	
	else:
		None
		
	return None
	
	
def button_validation_generateur_de_calcul(sender):
	"""
	button_validation_generateur_de_calcul : sender -> None
	button_validation_generateur_de_calcul(sender) si le compteur est inférieur à 10, appel de la fonction generateur_de_calculs_aleatoires(), affecte +1 à la variable globale nbre_de_victoires_generateur_de_calcul si le résultat est correct, sinon, None. Affecte +1 à la variable globale compteur_generateur_de_calcul.
	"""
	global view_preparation_generateur_de_calcul
	global view_generateur_de_calcul
	global view_resultats_tests
	global button_principal_generateur_de_calcul
	global liste_resultat_generateur_de_calcul
	global calculs_aleatoires
	global nbre_de_victoires_generateur_de_calcul
	global compteur_generateur_de_calcul
	global resultat_generateur_de_calcul
	global temps_arret_generateur_de_calcul
	global duree_execution_generateur_de_calcul
	global duree_execution_jeu_hexagones
	x = calculs_aleatoires[0]
	y = calculs_aleatoires[1]
	signe_calcul_aleatoire = calculs_aleatoires[2]
	
	# Affectation du résultat numerique du calcul à la variable resultat_numerique_generateur_de_calcul.
	if signe_calcul_aleatoire == '+':
		resultat_numerique_generateur_de_calcul = x + y
	elif signe_calcul_aleatoire == '-':
		resultat_numerique_generateur_de_calcul = x - y
	elif signe_calcul_aleatoire == 'x':
		resultat_numerique_generateur_de_calcul = x * y
		
	if button_principal_generateur_de_calcul.title != 'Tap to Start':
	
		if len(liste_resultat_generateur_de_calcul) != 0 and liste_resultat_generateur_de_calcul != ['-']:
			resultat_utilisateur = int(''.join(liste_resultat_generateur_de_calcul))
			
			if compteur_generateur_de_calcul < 10:
				if resultat_numerique_generateur_de_calcul == resultat_utilisateur:
					sound.play_effect('ApplePay sound effect.m4a')
					nbre_de_victoires_generateur_de_calcul += 1
					compteur_generateur_de_calcul += 1
					
					calculs_aleatoires = generateur_de_calculs_aleatoires()
					x = calculs_aleatoires[0]
					y = calculs_aleatoires[1]
					signe_calcul_aleatoire = calculs_aleatoires[2]
					
					button_principal_generateur_de_calcul.title = '{} {} {}'.format(x, signe_calcul_aleatoire, y)
					button_principal_generateur_de_calcul.action = button_principal_generateur_de_calcul_v2
					
					liste_resultat_generateur_de_calcul = []
					resultat_generateur_de_calcul.text = ''
					
				else:
					sound.play_effect('game:Error')
					compteur_generateur_de_calcul += 1
					
					calculs_aleatoires = generateur_de_calculs_aleatoires()
					x = calculs_aleatoires[0]
					y = calculs_aleatoires[1]
					signe_calcul_aleatoire = calculs_aleatoires[2]
					
					button_principal_generateur_de_calcul.title = '{} {} {}'.format(x,signe_calcul_aleatoire, y)
					button_principal_generateur_de_calcul.action = button_principal_generateur_de_calcul_v2
					
					liste_resultat_generateur_de_calcul = []
					resultat_generateur_de_calcul.text = ''
					
			else:
				temps_arret_generateur_de_calcul = time.time()
				traitement_resultat_generateur_de_calculs()
				
				if duree_execution_jeu_hexagones != 1: 
					sound.play_effect('ApplePay sound effect.m4a')
					resultats_tests()
					view_preparation_generateur_de_calcul.add_subview(view_resultats_tests)
	
				else:
					sound.play_effect('ApplePay sound effect.m4a')
					view_generateur_de_calcul.remove_subview(view_preparation_generateur_de_calcul)
				
		else:
			None
						
			
def generateur_de_calculs_aleatoires():
	"""
	generateur_de_calculs_aleatoires : None -> List[int,int,str]
	generateur_de_calculs_aleatoires() retourne la liste paire_de_chiffres_aleatoires[int,int,str].
	"""
	global calculs_aleatoires
	paire_de_chiffres_aleatoires = []
	
	x = r.randint(-20, 20)
	y = r.randint(0, 15)
	
	paire_de_chiffres_aleatoires.append(x)
	paire_de_chiffres_aleatoires.append(y)
	
	# Séléction aléatoire du signe.
	if -10 <= x <= 10 and y <= 10:
		selection_operation_aleatoire = r.randint(1,3)
		
		if selection_operation_aleatoire == 1:
			paire_de_chiffres_aleatoires.append('x')
		elif selection_operation_aleatoire == 2:
			paire_de_chiffres_aleatoires.append('-')
		elif selection_operation_aleatoire == 3:
			paire_de_chiffres_aleatoires.append('+')
			
	else:
		selection_operation_aleatoire = r.randint(1,2)
		
		if selection_operation_aleatoire == 1:
			paire_de_chiffres_aleatoires.append('+')
		elif selection_operation_aleatoire == 2:
			paire_de_chiffres_aleatoires.append('-')
			
	return paire_de_chiffres_aleatoires
	
	
def traitement_resultat_generateur_de_calculs():
	"""
	traitement_resultat_generateur_de_calculs : None -> None
	traitement_resultat_generateur_de_calculs(sender) Affecte à la variable globale duree_execution_generateur_de_calcul, la durée mise par le joueur pour réaliser les 10 calculs. Return None.
	"""
	global temps_demarrage_generateur_de_calcul
	global temps_arret_generateur_de_calcul
	global duree_execution_generateur_de_calcul
	
	duree_execution_generateur_de_calcul = temps_arret_generateur_de_calcul - temps_demarrage_generateur_de_calcul
	duree_execution_generateur_de_calcul = round(duree_execution_generateur_de_calcul, 2)
	
	return None

		
"""
View Preparation_jeu_hexagones. Affiche les consignes du test avec les hexagones et 1 bouton. Ajoute la sous-vue view_jeu_hexagones. Affecte à la variable globale temps_demarrage_jeu_hexagones, le temps au moment de l'appel.
"""

def button_1_preparation_jeu_hexagones(sender):
	"""
	button_1_preparation_jeu_hexagones : sender -> None
	button_1_preparation_jeu_hexagones(sender) ajoute la sous-vue view_jeu_hexagones à la sous_vue view_preparation_jeu_hexagones, stocke le temps au moment de l'appel de la fonction dans la variable temps_demarrage_jeu_hexagones, return None.
	"""
	global view_preparation_jeu_hexagones
	global view_jeu_hexagones
	global temps_demarrage_jeu_hexagones
	
	temps_demarrage_jeu_hexagones = time.time()
	
	speech.say('Allons y', 'fr-FR') # Réalise la dictée du message en français.
	view_preparation_jeu_hexagones.add_subview(view_jeu_hexagones)
	
	return None
	
	
"""
View jeu_hexagones. Affiche 4 à 5 boutons et images à l'ecran, selon des positions aléatoires. Le jeu s'arrête au terme de 10 séries.
"""

def button_1_jeu_hexagones_tapped(sender):
	"""
	button_1_jeu_hexagones_tapped : sender -> None
	button_1_jeu_hexagones_tapped(sender) Si le bouton est plus petit que les autres, il disparait, si il était le seul à l'ecran, affecte +1 à la variable nbre_reussites_jeu_hexagones et appel de la fonction resultats_jeu_hexagones(). Sinon, appel de la fonction resultats_jeu_hexagones(), son d'erreur. Return None.
	"""
	global button_1_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global nbre_reussites_jeu_hexagones
	
	view_jeu_hexagones.remove_subview(button_1_jeu_hexagones)
	view_jeu_hexagones.remove_subview(imageview1_jeu_hexagones)
	view_jeu_hexagones.remove_subview(label_1_jeu_hexagones)
	
	indice_presence_button_1 = 0
	
	if valeur_button_1_jeu_hexagones < valeur_button_2_jeu_hexagones and valeur_button_1_jeu_hexagones < valeur_button_3_jeu_hexagones and valeur_button_1_jeu_hexagones < valeur_button_4_jeu_hexagones and valeur_button_1_jeu_hexagones < valeur_button_5_jeu_hexagones:
	
		sound.play_effect('ApplePay sound effect.m4a')
		valeur_button_1_jeu_hexagones = 21
		
		if indice_presence_button_2 == 1 or indice_presence_button_3 == 1 or indice_presence_button_4 == 1 or indice_presence_button_5 == 1:	
			
			None
			
		else:
			nbre_reussites_jeu_hexagones += 1
			resultats_jeu_hexagones()
			
	else:
		sound.play_effect('game:Error')
		resultats_jeu_hexagones()
			
	return None
	
	
def button_2_jeu_hexagones_tapped(sender):
	"""
	button_2_jeu_hexagones_tapped : sender -> None
	button_2_jeu_hexagones_tapped(sender) Si le boutons est plus petit que les autres, il disparait, si il était le seul à l'ecran, affecte +1 à la variable nbre_reussites_jeu_hexagones et appel de la fonction resultats_jeu_hexagones(). Sinon, appel de la fonction resultats_jeu_hexagones(), son d'erreur. Return None.
	"""
	global button_2_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global nbre_reussites_jeu_hexagones
	
	view_jeu_hexagones.remove_subview(button_2_jeu_hexagones)
	view_jeu_hexagones.remove_subview(imageview2_jeu_hexagones)
	view_jeu_hexagones.remove_subview(label_2_jeu_hexagones)
	
	indice_presence_button_2 = 0
	
	if valeur_button_2_jeu_hexagones < valeur_button_1_jeu_hexagones and valeur_button_2_jeu_hexagones < valeur_button_3_jeu_hexagones and valeur_button_2_jeu_hexagones < valeur_button_4_jeu_hexagones and valeur_button_2_jeu_hexagones < valeur_button_5_jeu_hexagones:
	
		sound.play_effect('ApplePay sound effect.m4a')
		valeur_button_2_jeu_hexagones = 21
		
		if indice_presence_button_1 == 1 or indice_presence_button_3 == 1 or indice_presence_button_4 == 1 or indice_presence_button_5 == 1:	
		
			None
			
		else:
			nbre_reussites_jeu_hexagones += 1
			resultats_jeu_hexagones()
			
	else:
		sound.play_effect('game:Error')
		resultats_jeu_hexagones()
		
	return None
	
	
def button_3_jeu_hexagones_tapped(sender):
	"""
	button_3_jeu_hexagones_tapped : sender -> None
	button_3_jeu_hexagones_tapped(sender) Si le boutons est plus petit que les autres, il disparait, si il était le seul à l'ecran, affecte +1 à la variable nbre_reussites_jeu_hexagones et appel de la fonction resultats_jeu_hexagones(). Sinon, appel de la fonction resultats_jeu_hexagones(), son d'erreur. Return None.
	"""
	global button_3_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global nbre_reussites_jeu_hexagones
	
	view_jeu_hexagones.remove_subview(button_3_jeu_hexagones)
	view_jeu_hexagones.remove_subview(imageview3_jeu_hexagones)
	view_jeu_hexagones.remove_subview(label_3_jeu_hexagones)
	
	indice_presence_button_3 = 0
	
	if valeur_button_3_jeu_hexagones < valeur_button_1_jeu_hexagones and valeur_button_3_jeu_hexagones < valeur_button_2_jeu_hexagones and valeur_button_3_jeu_hexagones < valeur_button_4_jeu_hexagones and valeur_button_3_jeu_hexagones < valeur_button_5_jeu_hexagones:
	
		sound.play_effect('ApplePay sound effect.m4a')
		valeur_button_3_jeu_hexagones = 21
		
		if indice_presence_button_1 == 1 or indice_presence_button_2 == 1 or indice_presence_button_4 == 1 or indice_presence_button_5 == 1:
		
			None
			
		else:
			nbre_reussites_jeu_hexagones += 1
			resultats_jeu_hexagones()
			
	else:
		sound.play_effect('game:Error')
		resultats_jeu_hexagones()
		
	return None
	
	
def button_4_jeu_hexagones_tapped(sender):
	"""
	button_4_jeu_hexagones_tapped : sender -> None
	button_4_jeu_hexagones_tapped(sender) Si le boutons est plus petit que les autres, il disparait, si il était le seul à l'ecran, affecte +1 à la variable nbre_reussites_jeu_hexagones et appel de la fonction resultats_jeu_hexagones(). Sinon, appel de la fonction resultats_jeu_hexagones(), son d'erreur. Return None.
	"""
	global button_4_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global nbre_reussites_jeu_hexagones
	
	view_jeu_hexagones.remove_subview(button_4_jeu_hexagones)
	view_jeu_hexagones.remove_subview(imageview4_jeu_hexagones)
	view_jeu_hexagones.remove_subview(label_4_jeu_hexagones)
	
	indice_presence_button_4 = 0
	
	if valeur_button_4_jeu_hexagones < valeur_button_1_jeu_hexagones and valeur_button_4_jeu_hexagones < valeur_button_2_jeu_hexagones and valeur_button_4_jeu_hexagones < valeur_button_3_jeu_hexagones and valeur_button_4_jeu_hexagones < valeur_button_5_jeu_hexagones:
	
		sound.play_effect('ApplePay sound effect.m4a')
		valeur_button_4_jeu_hexagones = 21
		
		if indice_presence_button_1 == 1 or indice_presence_button_2 == 1 or indice_presence_button_3 == 1:
		
			None
			
		else:
			nbre_reussites_jeu_hexagones += 1
			resultats_jeu_hexagones()
			
	else:
		sound.play_effect('game:Error')
		resultats_jeu_hexagones()
		
	return None
	
	
def button_5_jeu_hexagones_tapped(sender):
	"""
	button_5_jeu_hexagones_tapped : sender -> None
	button_5_jeu_hexagones_tapped(sender) Si le boutons est plus petit que les autres, il disparait, si il était le seul à l'ecran, affecte +1 à la variable nbre_reussites_jeu_hexagones et appel de la fonction resultats_jeu_hexagones(). Sinon, appel de la fonction resultats_jeu_hexagones(), son d'erreur. Return None.
	"""
	global button_5_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global nbre_reussites_jeu_hexagones
	
	view_jeu_hexagones.remove_subview(button_5_jeu_hexagones)
	view_jeu_hexagones.remove_subview(imageview5_jeu_hexagones)
	view_jeu_hexagones.remove_subview(label_5_jeu_hexagones)
	
	indice_presence_button_5 = 0
	
	if valeur_button_5_jeu_hexagones < valeur_button_1_jeu_hexagones and valeur_button_5_jeu_hexagones < valeur_button_2_jeu_hexagones and valeur_button_5_jeu_hexagones < valeur_button_3_jeu_hexagones and valeur_button_5_jeu_hexagones < valeur_button_4_jeu_hexagones :
	
		sound.play_effect('ApplePay sound effect.m4a')
		valeur_button_5_jeu_hexagones = 21
		
		if indice_presence_button_1 == 1 or indice_presence_button_2 == 1 or indice_presence_button_3 == 1 or indice_presence_button_4 == 1:
			None
			
		else:
			nbre_reussites_jeu_hexagones += 1
			resultats_jeu_hexagones()
	
	else:
		sound.play_effect('game:Error')
		resultats_jeu_hexagones()
		
	return None
	
	
def generateur_de_position_jeu_hexagones():
	"""
	generateur_de_position_jeu_hexagones : None -> None
	generateur_de_position_jeu_hexagones() determine de manière aléatoire la position des 5 boutons et 5 images à partir du tuple tuple_positions_jeu_hexagones, return None.
	"""
	global button_1_jeu_hexagones
	global button_2_jeu_hexagones
	global button_3_jeu_hexagones
	global button_4_jeu_hexagones
	global button_5_jeu_hexagones
	global imageview1_jeu_hexagones
	global imageview2_jeu_hexagones
	global imageview3_jeu_hexagones
	global imageview4_jeu_hexagones
	global imageview5_jeu_hexagones
	global tuple_positions_jeu_hexagones
	global compteur_jeu_hexagones
	
	position_button_1_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
	
	
	imageview1_jeu_hexagones.x = position_button_1_jeu_hexagones[0]
	imageview1_jeu_hexagones.y =position_button_1_jeu_hexagones[1]
	
	button_1_jeu_hexagones.x = position_button_1_jeu_hexagones[0]
	button_1_jeu_hexagones.y = position_button_1_jeu_hexagones[1]
	
	label_1_jeu_hexagones.x = position_button_1_jeu_hexagones[0] + 10
	label_1_jeu_hexagones.y = position_button_1_jeu_hexagones[1] + 23
	
	
	position_button_2_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
	
	while position_button_2_jeu_hexagones == position_button_1_jeu_hexagones:
		position_button_2_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
		
	imageview2_jeu_hexagones.x = position_button_2_jeu_hexagones[0]
	imageview2_jeu_hexagones.y =position_button_2_jeu_hexagones[1]
	
	button_2_jeu_hexagones.x = position_button_2_jeu_hexagones[0]
	button_2_jeu_hexagones.y = position_button_2_jeu_hexagones[1]
	
	label_2_jeu_hexagones.x = position_button_2_jeu_hexagones[0] + 10
	label_2_jeu_hexagones.y = position_button_2_jeu_hexagones[1] + 23
	
	position_button_3_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
	
	while position_button_3_jeu_hexagones == position_button_1_jeu_hexagones or position_button_3_jeu_hexagones == position_button_2_jeu_hexagones:
	
		position_button_3_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
		
	imageview3_jeu_hexagones.x = position_button_3_jeu_hexagones[0]
	imageview3_jeu_hexagones.y =position_button_3_jeu_hexagones[1]
	
	button_3_jeu_hexagones.x = position_button_3_jeu_hexagones[0]
	button_3_jeu_hexagones.y = position_button_3_jeu_hexagones[1]
	
	label_3_jeu_hexagones.x = position_button_3_jeu_hexagones[0] + 10
	label_3_jeu_hexagones.y = position_button_3_jeu_hexagones[1] + 23
	
	position_button_4_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
	
	while position_button_4_jeu_hexagones == position_button_1_jeu_hexagones or position_button_4_jeu_hexagones == position_button_2_jeu_hexagones or position_button_4_jeu_hexagones == position_button_3_jeu_hexagones:
	
		position_button_4_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
		
	imageview4_jeu_hexagones.x = position_button_4_jeu_hexagones[0]
	imageview4_jeu_hexagones.y =position_button_4_jeu_hexagones[1]
	
	button_4_jeu_hexagones.x = position_button_4_jeu_hexagones[0]
	button_4_jeu_hexagones.y = position_button_4_jeu_hexagones[1]
	
	label_4_jeu_hexagones.x = position_button_4_jeu_hexagones[0] + 10
	label_4_jeu_hexagones.y = position_button_4_jeu_hexagones[1] + 23
	
	if compteur_jeu_hexagones >= 5:
		position_button_5_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
		
		while position_button_5_jeu_hexagones == position_button_1_jeu_hexagones or position_button_5_jeu_hexagones == position_button_2_jeu_hexagones or position_button_5_jeu_hexagones == position_button_3_jeu_hexagones or position_button_5_jeu_hexagones == position_button_4_jeu_hexagones:
		
			position_button_5_jeu_hexagones = r.choice(tuple_positions_jeu_hexagones)
			
		imageview5_jeu_hexagones.x = position_button_5_jeu_hexagones[0]
		imageview5_jeu_hexagones.y =position_button_5_jeu_hexagones[1]
		
		button_5_jeu_hexagones.x = position_button_5_jeu_hexagones[0]
		button_5_jeu_hexagones.y = position_button_5_jeu_hexagones[1]
		
		label_5_jeu_hexagones.x = position_button_5_jeu_hexagones[0] + 10
		label_5_jeu_hexagones.y = position_button_5_jeu_hexagones[1] + 23
		
	return None
	
	
def generateur_de_chiffres_jeu_hexagones():
	"""
	generateur_de_chiffres_jeu_hexagones : None -> None
	generateur_de_chiffres_jeu_hexagones() determine de manière aléatoire les nombres des 5 boutons, return None.
	"""
	global label_1_jeu_hexagones
	global label_2_jeu_hexagones
	global label_3_jeu_hexagones
	global label_4_jeu_hexagones
	global label_5_jeu_hexagones
	global valeur_button_1_jeu_hexagones
	global valeur_button_2_jeu_hexagones
	global valeur_button_3_jeu_hexagones
	global valeur_button_4_jeu_hexagones
	global valeur_button_5_jeu_hexagones
	global compteur_jeu_hexagones
	
	chiffre_button_1 = str(r.randint(0, 20))
	label_1_jeu_hexagones.text = chiffre_button_1
	valeur_button_1_jeu_hexagones = int(label_1_jeu_hexagones.text)
	
	chiffre_button_2 = str(r.randint(0, 20))
	
	while chiffre_button_2 == chiffre_button_1:
		chiffre_button_2 = str(r.randint(0, 20))
		
	label_2_jeu_hexagones.text = chiffre_button_2
	valeur_button_2_jeu_hexagones = int(label_2_jeu_hexagones.text)
	
	chiffre_button_3 = str(r.randint(0, 20))
	
	while chiffre_button_3 == chiffre_button_1 or chiffre_button_3 == chiffre_button_2:
		chiffre_button_3 = str(r.randint(0, 20))
		
	label_3_jeu_hexagones.text = chiffre_button_3
	valeur_button_3_jeu_hexagones = int(label_3_jeu_hexagones.text)
	
	chiffre_button_4 = str(r.randint(0, 20))
	
	while chiffre_button_4 == chiffre_button_1 or chiffre_button_4 == chiffre_button_2 or chiffre_button_4 == chiffre_button_3:
		chiffre_button_4 = str(r.randint(0, 20))
		
	label_4_jeu_hexagones.text = chiffre_button_4
	valeur_button_4_jeu_hexagones = int(label_4_jeu_hexagones.text)
	
	if compteur_jeu_hexagones > 5:
		chiffre_button_5 = str(r.randint(0, 20))
		
		while chiffre_button_5 == chiffre_button_1 or chiffre_button_5 == chiffre_button_2 or chiffre_button_5 == chiffre_button_3 or chiffre_button_5 == chiffre_button_4:
			chiffre_button_5 = str(r.randint(0, 20))
			
		label_5_jeu_hexagones.text = chiffre_button_5
		valeur_button_5_jeu_hexagones = int(label_5_jeu_hexagones.text)
		
	return None
	
	
def resultats_jeu_hexagones():
	"""
	resultats_jeu_hexagones : None -> None
	resultats_jeu_hexagones() si le compteur est inferieur à 10, appel des fonction generateur_de_chiffres_jeu_hexagones() et generateur_de_position_jeu_hexagones(), ajout des boutons et images à la sous-vue view_jeu_hexagones. Sinon, appel de la fonction traitement_resultat_jeu_hexagones(), si le generateur_de_calcul à deja été éxecute, ajout de la sous-vue view_resultats_tests, sinon, remove la sous-vue view_preparation_jeu_hexagones. Return None.
	"""	
	global view_jeu_hexagones
	global button_1_jeu_hexagones
	global button_2_jeu_hexagones
	global button_3_jeu_hexagones
	global button_4_jeu_hexagones
	global button_5_jeu_hexagones
	global imageview1_jeu_hexagones
	global imageview2_jeu_hexagones
	global imageview3_jeu_hexagones
	global imageview4_jeu_hexagones
	global imageview5_jeu_hexagones
	global label_1_jeu_hexagones
	global label_2_jeu_hexagones
	global label_3_jeu_hexagones
	global label_4_jeu_hexagones
	global label_5_jeu_hexagones
	global indice_presence_button_1
	global indice_presence_button_2
	global indice_presence_button_3
	global indice_presence_button_4
	global indice_presence_button_5
	global label_score_jeu_hexagones
	global temps_arret_jeu_hexagones
	global nbre_reussites_jeu_hexagones
	global compteur_jeu_hexagones
	
	label_score_jeu_hexagones.text = str(compteur_jeu_hexagones)
	compteur_jeu_hexagones += 1
	
	if compteur_jeu_hexagones <= 11:	
		generateur_de_chiffres_jeu_hexagones()
		generateur_de_position_jeu_hexagones()
		
		view_jeu_hexagones.add_subview(button_1_jeu_hexagones)
		view_jeu_hexagones.add_subview(imageview1_jeu_hexagones)
		view_jeu_hexagones.add_subview(label_1_jeu_hexagones)
		
		view_jeu_hexagones.add_subview(button_2_jeu_hexagones)
		view_jeu_hexagones.add_subview(imageview2_jeu_hexagones)
		view_jeu_hexagones.add_subview(label_2_jeu_hexagones)
		
		view_jeu_hexagones.add_subview(button_3_jeu_hexagones)
		view_jeu_hexagones.add_subview(imageview3_jeu_hexagones)
		view_jeu_hexagones.add_subview(label_3_jeu_hexagones)
		
		view_jeu_hexagones.add_subview(button_4_jeu_hexagones)
		view_jeu_hexagones.add_subview(imageview4_jeu_hexagones)
		view_jeu_hexagones.add_subview(label_4_jeu_hexagones)
		
		if compteur_jeu_hexagones > 5:
			view_jeu_hexagones.add_subview(button_5_jeu_hexagones)
			view_jeu_hexagones.add_subview(imageview5_jeu_hexagones)
			view_jeu_hexagones.add_subview(label_5_jeu_hexagones)
			indice_presence_button_5 = 1
			
	else:
		
		temps_arret_jeu_hexagones = time.time()
		traitement_resultat_jeu_hexagones()
		
		if duree_execution_generateur_de_calcul != 1: 
			sound.play_effect('Bottle open sound.m4a')
			resultats_tests()
			view_jeu_hexagones.add_subview(view_resultats_tests)
		else:
			view_jeu_hexagones.remove_subview(view_preparation_jeu_hexagones)
	
	# Remise à 0 des indices de présence des boutons.		
	indice_presence_button_1 = 1
	indice_presence_button_2 = 1
	indice_presence_button_3 = 1
	indice_presence_button_4 = 1
	
	return None

		
def traitement_resultat_jeu_hexagones():
	"""
	traitement_resultat_jeu_hexagones : None -> None
	traitement_resultat_jeu_hexagones(sender) Affecte à la variable globale duree_execution_jeu_hexagones, la durée mise par le joueur pour réaliser les 10 séries. Return None.
	"""
	global temps_demarrage_jeu_hexagones
	global temps_arret_jeu_hexagones
	global duree_execution_jeu_hexagones
	
	duree_execution_jeu_hexagones = temps_arret_jeu_hexagones - temps_demarrage_jeu_hexagones
	duree_execution_jeu_hexagones = round(duree_execution_jeu_hexagones, 2)

	return None

	
"""
View resultats_tests. Affiche 8 label, 1 bouton. L'utilisateur peut alors savoir si ses capacités intellectuelles sont suffisantes ou non.
"""

def resultats_tests():
	"""
	resultats_tests : None -> None
	resultats_tests() En fonction des résultats de l'utiliateur, affiche 8 labels, return None.
	"""
	global label_5_resultats_tests
	global label_6_resultats_tests
	global label_7_resultats_tests
	global label_8_resultats_tests
	global duree_execution_generateur_de_calcul
	global duree_execution_jeu_hexagones
	global nbre_de_victoires_generateur_de_calcul
	global nbre_reussites_jeu_hexagones
	
	if nbre_de_victoires_generateur_de_calcul < 5 or nbre_reussites_jeu_hexagones < 5 or duree_execution_generateur_de_calcul > 50.0 or duree_execution_jeu_hexagones > 40:
		label_4_resultats_tests.text = 'Vous n’êtes pas au maximum de'
		label_5_resultats_tests.text = 'vos capacités intellectuelles.'
		label_6_resultats_tests.text = 'Nous vous déconseillons fortement'
		label_7_resultats_tests.text = 'l’usage de tous moyens de transport.'
		label_8_resultats_tests.text = 'Favorisez le covoiturage !'
	
	else:
		label_4_resultats_tests.text = 'Vous êtes en bonne disposition'
		label_5_resultats_tests.text = 'psychologique.'

	return None
	
	
"""
Definition des boutons, vues et listes en tant que variables globales.
"""

view_menu_principal = ui.load_view('Menu_principal')


view_genre = ui.load_view('Genre_calculatrice')
view_soundcloud_calculatrice = ui.load_view('Soundcloud')
view_uber_calculatrice = ui.load_view('Uber')
view_calculatrice_poids = ui.load_view('Calculatrice_poids')
view_classes = ui.load_view('Classe_calculatrice')


view_marques_bieres = ui.load_view('Marques_bieres')
view_volumes_bieres = ui.load_view('Volumes_bieres')

view_categories_spiritueux = ui.load_view('Categories_spiritueux')
view_volumes_spiritueux = ui.load_view('Volumes_spiritueux')
view_gin_calculatrice = ui.load_view('Gin_calculatrice')
view_liqueurs_calculatrice = ui.load_view('Liqueurs_calculatrice')
view_rhum_calculatrice = ui.load_view('Rhum_calculatrice')
view_vodka_calculatrice = ui.load_view('Vodka_calculatrice')

view_categories_vins = ui.load_view('Categories_vins')
view_volumes_vins = ui.load_view('Volumes_vins')

view_boucle_calculatrice = ui.load_view('Boucle_calculatrice')
view_resultat_calculatrice = ui.load_view('Resultat_calculatrice')


view_preparation_generateur_de_calcul = ui.load_view('Preparation generateur de calcul')
generateur_de_calcul = ui.load_view('Generateur de calcul') # Chargement de la vue 'Generateur de calcul'.


view_preparation_jeu_hexagones = ui.load_view('Preparation jeu hexagones')
view_jeu_hexagones = ui.load_view('Jeu_hexagones')


view_resultats_tests = ui.load_view('Resultats tests')

# View menu_principal.

button_1_menu_principal = view_menu_principal.subviews[1]
button_2_menu_principal = view_menu_principal.subviews[2]
button_3_menu_principal = view_menu_principal.subviews[3]
button_soundcloud_calculatrice = view_menu_principal.subviews[4]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View genre.

label_genre_calculatrice = view_genre.subviews[1]
button_homme_calculatrice = view_genre.subviews[2]
button_femme_calculatrice = view_genre.subviews[3]
button_soundcloud_calculatrice = view_genre.subviews[4]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')
coefficient_de_diffusion_k = 0

# View soundcloud_calculatrice.

page_souncloud_calculatrice = view_soundcloud_calculatrice.subviews[0]
button_retour_calculatrice = view_soundcloud_calculatrice.subviews[1]

# View calculatrice_poids.

calculatrice_view = view_calculatrice_poids.subviews[0]
label_principal = view_calculatrice_poids.subviews[1]
champs_de_texte_calculatrice = view_calculatrice_poids.subviews[2]
button_validation_calculatrice = view_calculatrice_poids.subviews[3]
button_1_calculatrice = view_calculatrice_poids.subviews[4]
button_2_calculatrice = view_calculatrice_poids.subviews[5]
button_3_calculatrice = view_calculatrice_poids.subviews[6]
button_4_calculatrice = view_calculatrice_poids.subviews[7]
button_5_calculatrice = view_calculatrice_poids.subviews[8]
button_6_calculatrice = view_calculatrice_poids.subviews[9]
button_7_calculatrice = view_calculatrice_poids.subviews[10]
button_8_calculatrice = view_calculatrice_poids.subviews[11]
button_9_calculatrice = view_calculatrice_poids.subviews[12]
button_0_calculatrice = view_calculatrice_poids.subviews[13]
button_delete_calculatrice = view_calculatrice_poids.subviews[14]
button_soundcloud_calculatrice = view_calculatrice_poids.subviews[16]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')
liste_calculatrice = []
champs_de_texte_calculatrice.text = ''
poids_utilisateur = 0

# View classes.

label_classe_calculatrice = view_classes.subviews[1]
button_bieres_calculatrice = view_classes.subviews[2]
button_spiritueux_calculatrice = view_classes.subviews[3]
button_vins_calculatrice = view_classes.subviews[4]
button_soundcloud_calculatrice = view_classes.subviews[5]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View marques_bieres.

slider_marques_bieres = view_marques_bieres.subviews[1]
button_1_marques_bieres = view_marques_bieres.subviews[2]
button_2_marques_bieres = view_marques_bieres.subviews[3]
button_3_marques_bieres = view_marques_bieres.subviews[4]
button_4_marques_bieres = view_marques_bieres.subviews[5]
label_marques_bieres = view_marques_bieres.subviews[6]
button_soundcloud_calculatrice = view_marques_bieres.subviews[7]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View volumes_bieres.

label_volumes_bieres = view_volumes_bieres.subviews[1]
label_bouteilles = view_volumes_bieres.subviews[2]
slider_bouteilles = view_volumes_bieres.subviews[3]
label_nbre_bouteilles = view_volumes_bieres.subviews[4]
label_petites_canettes = view_volumes_bieres.subviews[5]
slider_petites_canettes = view_volumes_bieres.subviews[6]
label_nbre_petites_canettes = view_volumes_bieres.subviews[7]
label_gandes_canettes = view_volumes_bieres.subviews[8]
slider_grandes_canettes = view_volumes_bieres.subviews[9]
label_nbre_grandes_canettes = view_volumes_bieres.subviews[10]
button_validation_volumes_bieres = view_volumes_bieres.subviews[11]
button_soundcloud_calculatrice = view_volumes_bieres.subviews[12]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View categories_spiritueux.

slider_categories_spiritueux = view_categories_spiritueux.subviews[1]
button_1_categories_spiritueux = view_categories_spiritueux.subviews[2]
button_2_categories_spiritueux = view_categories_spiritueux.subviews[3]
button_3_categories_spiritueux = view_categories_spiritueux.subviews[4]
button_4_categories_spiritueux = view_categories_spiritueux.subviews[5]
label_categories_spiritueux = view_categories_spiritueux.subviews[6]
button_soundcloud_calculatrice = view_categories_spiritueux.subviews[7]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View volumes_spiritueux.

label_volumes_spiritueux = view_volumes_spiritueux.subviews[1]
label_demi_shot = view_volumes_spiritueux.subviews[2]
slider_demi_shot = view_volumes_spiritueux.subviews[3]
label_nbre_demi_shot = view_volumes_spiritueux.subviews[4]
label_shot = view_volumes_spiritueux.subviews[5]
slider_shot = view_volumes_spiritueux.subviews[6]
label_nbre_shot = view_volumes_spiritueux.subviews[7]
label_coktail = view_volumes_spiritueux.subviews[8]
slider_cocktail = view_volumes_spiritueux.subviews[9]
label_nbre_cocktail = view_volumes_spiritueux.subviews[10]
button_validation_volumes_spiritueux = view_volumes_spiritueux.subviews[11]
button_soundcloud_calculatrice = view_volumes_spiritueux.subviews[12]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View gin_calculatrice.

label_gin_calculatrice = view_gin_calculatrice.subviews[1]
button_1_gin_calculatrice = view_gin_calculatrice.subviews[2]
button_2_gin_calculatrice = view_gin_calculatrice.subviews[3]
button_3_gin_calculatrice = view_gin_calculatrice.subviews[4]
button_4_gin_calculatrice = view_gin_calculatrice.subviews[5]
button_soundcloud_calculatrice = view_gin_calculatrice.subviews[6]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View liqueurs_calculatrice.

label_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[1]
slider_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[2]
button_1_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[3]
button_2_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[4]
button_3_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[5]
button_4_liqueurs_calculatrice = view_liqueurs_calculatrice.subviews[6]
button_soundcloud_calculatrice = view_liqueurs_calculatrice.subviews[7]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View rhum_calculatrice.

label_rhum_calculatrice = view_rhum_calculatrice.subviews[1]
slider_rhum_calculatrice = view_rhum_calculatrice.subviews[2]
button_1_rhum_calculatrice = view_rhum_calculatrice.subviews[3]
button_2_rhum_calculatrice = view_rhum_calculatrice.subviews[4]
button_3_rhum_calculatrice = view_rhum_calculatrice.subviews[5]
button_4_rhum_calculatrice = view_rhum_calculatrice.subviews[6]
button_soundcloud_calculatrice = view_rhum_calculatrice.subviews[7]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View vodka_calculatrice.

label_vodka_calculatrice = view_vodka_calculatrice.subviews[1]
slider_vodka_calculatrice = view_vodka_calculatrice.subviews[2]
button_1_vodka_calculatrice = view_vodka_calculatrice.subviews[3]
button_2_vodka_calculatrice = view_vodka_calculatrice.subviews[4]
button_3_vodka_calculatrice = view_vodka_calculatrice.subviews[5]
button_4_vodka_calculatrice = view_vodka_calculatrice.subviews[6]
button_soundcloud_calculatrice = view_vodka_calculatrice.subviews[7]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View categories_vins.

label_categories_vins = view_categories_vins.subviews[1]
button_1_categories_vins = view_categories_vins.subviews[2]
button_2_categories_vins = view_categories_vins.subviews[3]
button_3_categories_vins = view_categories_vins.subviews[4]
button_4_categories_vins = view_categories_vins.subviews[5]
button_soundcloud_calculatrice = view_categories_vins.subviews[6]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View volumes_vins.

label_ballon = view_volumes_vins.subviews[2]
slider_ballon = view_volumes_vins.subviews[3]
label_nbre_ballon = view_volumes_vins.subviews[4]
label_verre = view_volumes_vins.subviews[5]
slider_verre = view_volumes_vins.subviews[6]
label_nbre_verre = view_volumes_vins.subviews[7]
label_cup = view_volumes_vins.subviews[8]
slider_cup = view_volumes_vins.subviews[9]
label_nbre_cup = view_volumes_vins.subviews[10]
button_validation_volumes_vins = view_volumes_vins.subviews[11]
button_soundcloud_calculatrice = view_volumes_vins.subviews[12]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View boucle_calculatrice.

label1_boucle_calculatrice = view_boucle_calculatrice.subviews[1]
label2_boucle_calculatrice = view_boucle_calculatrice.subviews[2]
button_oui_boucle_calculatrice = view_boucle_calculatrice.subviews[3]
button_non_boucle_calculatrice = view_boucle_calculatrice.subviews[4]
button_soundcloud_calculatrice = view_boucle_calculatrice.subviews[5]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')

# View resultat_calculatrice.

label1_resultat_calculatrice = view_resultat_calculatrice.subviews[1]
label2_resultat_calculatrice = view_resultat_calculatrice.subviews[2]
label3_resultat_calculatrice = view_resultat_calculatrice.subviews[3]
label4_resultat_calculatrice = view_resultat_calculatrice.subviews[4]
button_uber_calculatrice = view_resultat_calculatrice.subviews[5]
button_soundcloud_calculatrice = view_resultat_calculatrice.subviews[6]
button_soundcloud_calculatrice.image = ui.Image('Soundcloud_logo.PNG')
label7_resultat_calculatrice = view_resultat_calculatrice.subviews[9]
button_home_resultat_calculatrice = view_resultat_calculatrice.subviews[10]

degre_alcoolique = 0
masse_alcool_totale = 0

# View uber.

page_uber_calculatrice = view_uber_calculatrice.subviews[0]

# View preparation_generateur_de_calcul.

button_1_preparation_generateur_de_calcul = view_preparation_generateur_de_calcul.subviews[3]

# View _generateur_de_calcul.

view_generateur_de_calcul = generateur_de_calcul.subviews[0]
button_principal_generateur_de_calcul = generateur_de_calcul.subviews[1]
signe_egal_generateur_de_calcul = generateur_de_calcul.subviews[2]

button_1_generateur_de_calcul = generateur_de_calcul.subviews[3]
button_2_generateur_de_calcul = generateur_de_calcul.subviews[4]
button_3_generateur_de_calcul = generateur_de_calcul.subviews[5]
button_4_generateur_de_calcul = generateur_de_calcul.subviews[6]
button_5_generateur_de_calcul = generateur_de_calcul.subviews[7]
button_6_generateur_de_calcul = generateur_de_calcul.subviews[8]
button_7_generateur_de_calcul = generateur_de_calcul.subviews[9]
button_8_generateur_de_calcul = generateur_de_calcul.subviews[10]
button_9_generateur_de_calcul = generateur_de_calcul.subviews[11]
button_0_generateur_de_calcul = generateur_de_calcul.subviews[12]
button_negatif_generateur_de_calcul = generateur_de_calcul.subviews[13]
button_delete_generateur_de_calcul = generateur_de_calcul.subviews[14]
button_validation_generateur_de_calcul = generateur_de_calcul.subviews[15]

resultat_generateur_de_calcul = generateur_de_calcul.subviews[16]

liste_resultat_generateur_de_calcul = []
resultat_generateur_de_calcul.text = ''
nbre_de_victoires_generateur_de_calcul = 0
compteur_generateur_de_calcul = 0
calculs_aleatoires = generateur_de_calculs_aleatoires()

temps_demarrage_generateur_de_calcul = 0
temps_arret_generateur_de_calcul = 0
duree_execution_generateur_de_calcul = 1

# View preparation_jeu_hexagones.

button_1_preparation_jeu_hexagones = view_preparation_jeu_hexagones.subviews[1]

# View jeu_hexagones.

position_a_jeu_hexagones = (2, 20)
position_b_jeu_hexagones = (100, 20)
position_c_jeu_hexagones = (198, 20)
position_d_jeu_hexagones = (2, 125)
position_e_jeu_hexagones = (100, 125)
position_f_jeu_hexagones = (198, 125)
position_g_jeu_hexagones = (2, 230)
position_h_jeu_hexagones = (100, 230)
position_i_jeu_hexagones = (199, 230)
position_j_jeu_hexagones = (2, 335)
position_k_jeu_hexagones = (100, 335)
position_l_jeu_hexagones = (198, 335)

tuple_positions_jeu_hexagones = (position_a_jeu_hexagones, position_b_jeu_hexagones, position_c_jeu_hexagones, position_d_jeu_hexagones, position_e_jeu_hexagones, position_f_jeu_hexagones, position_g_jeu_hexagones, position_h_jeu_hexagones, position_i_jeu_hexagones, position_j_jeu_hexagones, position_k_jeu_hexagones, position_l_jeu_hexagones)

label_score_jeu_hexagones = view_jeu_hexagones.subviews[1]

imageview1_jeu_hexagones = ui.ImageView('IMG_0597.PNG')
imageview1_jeu_hexagones.image = ui.Image('IMG_0597.PNG')
imageview1_jeu_hexagones.width = 120
imageview1_jeu_hexagones.height = 140

imageview2_jeu_hexagones = ui.ImageView('IMG_0594.PNG')
imageview2_jeu_hexagones.image = ui.Image('IMG_0594.PNG')
imageview2_jeu_hexagones.width = 120
imageview2_jeu_hexagones.height = 140

imageview3_jeu_hexagones = ui.ImageView('IMG_0596.PNG')
imageview3_jeu_hexagones.image = ui.Image('IMG_0596.PNG')
imageview3_jeu_hexagones.width = 120
imageview3_jeu_hexagones.height = 140

imageview4_jeu_hexagones = ui.ImageView('IMG_0602.PNG')
imageview4_jeu_hexagones.image = ui.Image('IMG_0602.PNG')
imageview4_jeu_hexagones.width = 120
imageview4_jeu_hexagones.height = 140

imageview5_jeu_hexagones = ui.ImageView('IMG_0601.PNG')
imageview5_jeu_hexagones.image = ui.Image('IMG_0601.PNG')
imageview5_jeu_hexagones.width = 120
imageview5_jeu_hexagones.height = 140

button_1_jeu_hexagones = ui.Button(title = None, image = None, action = button_1_jeu_hexagones_tapped, enabled=True, tint_color=None)
button_1_jeu_hexagones.image = ui.Image('IMG_0597.PNG')
button_1_jeu_hexagones.width = 120
button_1_jeu_hexagones.height = 140

button_2_jeu_hexagones = ui.Button(title = None, image = None, action = button_2_jeu_hexagones_tapped, enabled=True, tint_color=None)
button_2_jeu_hexagones.image = ui.Image('IMG_0594.PNG')
button_2_jeu_hexagones.width = 120
button_2_jeu_hexagones.height = 140

button_3_jeu_hexagones = ui.Button(title = None, image = None, action = button_3_jeu_hexagones_tapped, enabled=True, tint_color=None)
button_3_jeu_hexagones.image = ui.Image('IMG_0596.PNG')
button_3_jeu_hexagones.width = 120
button_3_jeu_hexagones.height = 140

button_4_jeu_hexagones = ui.Button(title = None, image = None, action = button_4_jeu_hexagones_tapped, enabled=True, tint_color=None)
button_4_jeu_hexagones.image = ui.Image('IMG_0602.PNG')
button_4_jeu_hexagones.width = 120
button_4_jeu_hexagones.height = 140

button_5_jeu_hexagones = ui.Button(title = None, image = None, action = button_5_jeu_hexagones_tapped, enabled=True, tint_color=None)
button_5_jeu_hexagones.image = ui.Image('IMG_0601.PNG')
button_5_jeu_hexagones.width = 120
button_5_jeu_hexagones.height = 140

label_1_jeu_hexagones = ui.Label()
label_1_jeu_hexagones.alignment = ui.ALIGN_CENTER
label_1_jeu_hexagones.text_color = 'white'
label_1_jeu_hexagones.font = ('<System-Bold>', 45)
label_1_jeu_hexagones.width = 50
label_1_jeu_hexagones.width = 100

label_2_jeu_hexagones = ui.Label()
label_2_jeu_hexagones.alignment = ui.ALIGN_CENTER
label_2_jeu_hexagones.text_color = 'white'
label_2_jeu_hexagones.font = ('<System-Bold>', 45)
label_2_jeu_hexagones.width = 50
label_2_jeu_hexagones.width = 100

label_3_jeu_hexagones = ui.Label()
label_3_jeu_hexagones.alignment = ui.ALIGN_CENTER
label_3_jeu_hexagones.text_color = 'white'
label_3_jeu_hexagones.font = ('<System-Bold>', 45)
label_3_jeu_hexagones.width = 50
label_3_jeu_hexagones.width = 100

label_4_jeu_hexagones = ui.Label()
label_4_jeu_hexagones.alignment = ui.ALIGN_CENTER
label_4_jeu_hexagones.text_color = 'white'
label_4_jeu_hexagones.font = ('<System-Bold>', 45)
label_4_jeu_hexagones.width = 50
label_4_jeu_hexagones.width = 100

label_5_jeu_hexagones = ui.Label()
label_5_jeu_hexagones.alignment = ui.ALIGN_CENTER
label_5_jeu_hexagones.text_color = 'white'
label_5_jeu_hexagones.font = ('<System-Bold>', 45)
label_5_jeu_hexagones.width = 50
label_5_jeu_hexagones.width = 100

valeur_button_1_jeu_hexagones = 0
valeur_button_2_jeu_hexagones = 0
valeur_button_3_jeu_hexagones = 0
valeur_button_4_jeu_hexagones = 0
valeur_button_5_jeu_hexagones = 21 # Afin qu'il ne soit pas pris en compte les 5 premiers tours.

"""
indice_de_presence prend la valeur 1 lorsque le bouton est affiché a l'ecran.
"""

indice_presence_button_1 = 1
indice_presence_button_2 = 1
indice_presence_button_3 = 1
indice_presence_button_4 = 1
indice_presence_button_5 = 0

compteur_jeu_hexagones = 2

nbre_reussites_jeu_hexagones = 0

generateur_de_chiffres_jeu_hexagones()
generateur_de_position_jeu_hexagones()

view_jeu_hexagones.add_subview(button_1_jeu_hexagones)
view_jeu_hexagones.add_subview(imageview1_jeu_hexagones)
view_jeu_hexagones.add_subview(label_1_jeu_hexagones)

view_jeu_hexagones.add_subview(button_2_jeu_hexagones)
view_jeu_hexagones.add_subview(imageview2_jeu_hexagones)
view_jeu_hexagones.add_subview(label_2_jeu_hexagones)

view_jeu_hexagones.add_subview(button_3_jeu_hexagones)
view_jeu_hexagones.add_subview(imageview3_jeu_hexagones)
view_jeu_hexagones.add_subview(label_3_jeu_hexagones)

view_jeu_hexagones.add_subview(button_4_jeu_hexagones)
view_jeu_hexagones.add_subview(imageview4_jeu_hexagones)
view_jeu_hexagones.add_subview(label_4_jeu_hexagones)

temps_demarrage_jeu_hexagones = 0
temps_arret_jeu_hexagones = 0
duree_execution_jeu_hexagones = 1

# View resultats_tests.

label_1_resultats_tests = view_resultats_tests.subviews[1]
label_2_resultats_tests = view_resultats_tests.subviews[2]
label_3_resultats_tests = view_resultats_tests.subviews[3]
label_4_resultats_tests = view_resultats_tests.subviews[4]
label_5_resultats_tests = view_resultats_tests.subviews[5]
label_6_resultats_tests = view_resultats_tests.subviews[6]
label_7_resultats_tests = view_resultats_tests.subviews[7]
label_8_resultats_tests = view_resultats_tests.subviews[8]

# Chargement de la page Soundcloud en arrière-plan.
page_souncloud_calculatrice.load_url('https://m.soundcloud.com/stresametgrenadine')

# Présentation de la vue view_menu_principal.
view_menu_principal.present('sheet')
