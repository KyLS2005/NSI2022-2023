#### Calculs simple :  

Python permet de calculer différentes opération  
voici quelques exemples d'opérateurs   
- ' * ' pour multiplier   
- ' / ' pour diviser   
- ' + ' pour additionner   
- ' - ' pour soustraire  
 
_exemple :_

```python
1+2
```

_note: les parenthèse sont utilisables_  
Il y a les opérateurs de comparaison:  
'=='
'!='
'>='
'<='
'<'
'>'

## Les chaines de caractère  
  
Les **chaines de caractères** _(string)_ sont caractérisées par des **guillemets**.  
  
_exemple :_  

```python
'hello'
"hello"
```  
Elles peuvent **s'ajouter** entre elles en faisant une somme.  
  
_exemple :_  
```python
'hello' + 'world'
 ``` 
ce qui donnera :

```python
'helloworld'
 ``` 

On peut aussi rajouter un espace dans une chaine de caractère.  
  
_exemple :_
```python
'hello ' + 'world'

'hello' + ' world'

'hello' + ' ' + ' world'

```
_ce qui donne :_

```python
'hello world'
```
_! Attention a ne pas confondre une chaine vide avec une qui contient un espace_  

## L'éditeur  
**L'éditeur** permet d'exécuter des scripts beaucoup plus **long**
Python exécute les lignes de **haut en bas**
Les valeurs peuvent changer et plusieurs éléments peuvent être renvoyés.  
Les valeurs affichés ne se font pas de la même façon que dans la console.  
Si on ne marque que une chaine de caractère dans l'éditeur rien ne sera affiché.  
La commande **print()** quand elle permet de la renvoyer depuis l'éditeur.  

_note : une variable dépendente d'autres variables ne sera pas mis à jour si une de celles qui la compose évolue_   

## Les Variables 

Une **variable** est une valeur **inconnu** comme x ou n'importe quelle caractère ou suite de caractère.  
Elle permet de contenir certaines valeurs et peut évoluer au fur et à mesure de l'exécution.  
On la définie avec " = "

_exemple :_

```python
mot = 'Hello'
```

La variable mot fera donc appelle à ce qu'elle contient  
_**! Attention** si on met des guillemet cela sera considéré comme une **chaine de caractère** et non une variable_  
Si la variable n'est **pas** défini cela renvoiera un message d'erreur
on utilise "_" à la place des espaces pour les variables  


Une chaine de caractère et une variable en contenant une peuvent s'additionner.  
De même avec deux variables contenant le même type de valeur  
_exemple :_

```python
mot = 'Hello'
nom = 'World'

mot = mot + nom

print(mot)
```

on peut l'écrire plus simplement :  

```python
mot = 'Hello'
nom = 'World'

mot += nom

print(mot)
```
Il s'agit l'**incrémentation**, on peut remplacer le ' + ' par d'autre opérateurs  
Si on inverse la variable mot et nom on obtiendra un résultat différent:  

```python
mot = 'Hello'
nom = 'World'

mot = nom + mot

print(mot)
```
_note: on ne peut **pas** faire d'addition d'instruction_  
_exemple_ :

```python
(mot = 'Hello') + (nom = 'Bob')
```

## Les boucles 'For'  
  
Les boucles for sont constituées généralement d'une variable, d'un itérable et du code à répéter  

_exemples :_

```python
for caractere in nom: print(caractere)
```

'for', 'in' et ':' sont importants pour qu'une boucle puisse fonctionner  
cette même boucle peut s'écrire :
```python
nom = 'World'
for caractere in nom:
    print(caractere)
```
! attention à l'**indentation** pour que le code dans la boucle puisse être valide  
le code nom indenté s'exécutera après la boucle  
l'indentation est égale à 4 espaces plus simplement utilisez la touche "Tab" du clavier  

## Les structures conditionnelles  

Les **booléens** permettent de n'exécuter le code que sous certaines conditions.  
Il n'y en a que deux (True et False).  
Ceux-ci sont souvent utilisé dans des **structures conditionnelle if**.

```python
if <condition>:
    <corps>
``` 
on peut rajouter une partie facultative **'else'** qui si la condition du if n'est pas respecté alors il exécutera l'instruction du **bloc 'else'**

```python
condition = True
if condition:
    print('Oui')
else:
    print('Non')
``` 
on peut **imbriquer** des structures for et if
_exemple :_
```python
phrase = 'Hello World'
ravi = True


if ravi:
    nouvelle_phrase = ''
    for caractere in phrase:
        nouvelle_phrase += caractere + '!'
    phrase = nouvelle_phrase
print(phrase)
```
la fonction "elif " est un contractré de :
```python
else:
    if
```

### _Vocabulaire utile_  


**Une expression** : Une partie de code qui est évaluable et qui possède une valeur  
**évaluer** : C'est calculer la valeur d'une expression  
**l'itération** : C'est l'exécution d'une boucle   
**une instruction** est une ligne de code