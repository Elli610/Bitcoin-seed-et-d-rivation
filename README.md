# Bitcoin-seed-et-derivation

		Génération de clés, phrases mnémoniques et dérivation par Nathan HERVIER et Amaury MONGREVILLE


 	* Chacune des fonctions demandées ont été implémentées : 

- genere_priv : génére une clé privée de 128 bits de manière aléatoire
- seed_to_mnemo : transforme la clé privée en phrase mnémonique
- mnemo_to_seed : transforme une phrase mnémonique en clé privée
- master_priv : extrait la clé privée maîtresse et le chainCode maître à partir de la clé privée
- master_pub : extrait la clé publique maîtresse à partir de la clé privée
- genere_child : extrait la clée privée est le chaincode correspondant au niveau de dérivation et à l'index spécifiés 

Un menu est disponible à l'appel de la fonction main(). Il contient notamment un mode démonstration.


	* Etat du code
Toutes nos fonctions tournent à 2 petits problèmes prêts : 
 - il arrive que nos clés prennent moins de bits que prévu car puisqu'elles commencent par des 0, python les "simplifient". 
   il peut donc arriver qu'une clé n'ai pas la taille attendue.

 - Nos fonctions seed_to_mnemo et mnemo_to_seed créent des phrases mnémoniques valides (d'après le site que vous nous avez fournis). 
   Deplus, on peut envoyer une clé privée dans seed_to_mnemo() puis envoyer la phrase mnémonique dans mnemo_to_seed(). On obtiendra bien la première clé privée.
   Cependant, si on tranforme notre clé privée en phrase mnémonique sur le site que vous nous avez fournis, la phrase ne correspond pas. 



