# Analyse Business:

1. Utilisateur : Un utilisateur se connecte sur le site en fournissant ses informations d'identification. Un nouvel utilisateur doit s'inscrire avant d'accéder à la page d'accueil. Chaque utilisateur a un rôle qui peut être soit "passager", soit "admin". Les attributs d'un utilisateur peuvent inclure un identifiant unique, un nom, une adresse e-mail, un mot de passe et un rôle.
2. Page d'accueil : La page d'accueil affiche des informations pertinentes comme une liste de vols disponibles, le profil de l'utilisateur, les anciens vols de l'utilisateur, une liste de destinations populaires, et une liste dynamique des horaires des vols.
3. Réservation de vols : Un utilisateur avec le rôle de "passager" peut choisir de réserver un vol. Pour cela, il doit disposer d'un solde suffisant sur son compte. Le coût du vol est calculé en fonction de la distance à parcourir (tarif par kilomètre).
4. Gestion des vols : Un passager peut consulter la liste de ses vols réservés. Il a la possibilité de modifier ou d'annuler une réservation existante. De plus, il peut suivre le statut de son vol sur une carte en temps réel.
5. Notifications : Les utilisateurs reçoivent des notifications sur les changements d'état du vol, tels que les retards ou les annulations. Ces notifications sont envoyées à l'adresse e-mail associée à leur compte utilisateur.
6. Profil : Chaque utilisateur peut consulter et modifier son profil. Les informations de profil peuvent inclure le nom, l'adresse e-mail, le mot de passe, le solde du compte, l'historique des vols, etc.
7. Avion : Un avion a un modèle spécifique et une capacité définie (nombre de sièges). Il peut être en différents états, comme "disponible", "en vol" ou "en maintenance". Un avion est associé à un aéroport spécifique à un moment donné.
8. Aéroport : Un aéroport a un nom unique et un emplacement (ville, pays). Il a un certain nombre de pistes et de terminaux. A tout moment, un certain nombre d'avions sont présents à l'aéroport.
9.  Vol : Un vol est associé à un avion spécifique et suit un itinéraire précis. Il a un état, comme "en attente", "en vol" ou "terminé". Un vol a une liste de passagers, qui sont les utilisateurs ayant réservé ce vol.
10. Itinéraire : Un itinéraire comprend un aéroport de départ, un aéroport d'arrivée, une heure de départ et une heure d'arrivée prévue. Il peut également inclure une ou plusieurs escales.
11. Administrateur : Un administrateur a la capacité de gérer les avions et les aéroports. Il peut ajouter, modifier ou supprimer des avions et des aéroports. De plus, il peut réserver des vols pour le transport de marchandises. Enfin, un administrateur peut gérer les comptes utilisateurs, y compris la visualisation, la modification et la suppression des comptes.
12. Réservation : Une réservation représente une place réservée par un passager pour un vol spécifique. Elle a un état, comme "confirmée", "modifiée" ou "annulée". Une réservation est associée à un utilisateur spécifique et à un vol spécifique.
13. Billet : Un billet est généré après qu'une réservation a été confirmée. Il contient des informations spécifiques sur le vol (numéro de vol, heure de départ, heure d'arrivée), le passager (nom, identifiant) et les détails du siège (numéro de siège, classe - économique/affaires/première classe).
14. Historique des vols : Chaque utilisateur a un historique des vols qu'il a effectués. L'historique des vols pourrait inclure des informations telles que le numéro du vol, la date du vol, l'heure de départ, l'heure d'arrivée, la durée du vol, et l'état du vol.
15. Paiement : Lorsqu'un utilisateur réserve un vol, un paiement est effectué. Les détails du paiement incluent le montant payé, la date de paiement, le mode de paiement (carte de crédit, virement bancaire, etc.), et l'état du paiement (réussi, échoué).
16. Classe de siège : Chaque vol a un certain nombre de sièges, répartis en différentes classes (économique, affaires, première classe). Chaque classe a un prix différent.
17. Bagage : Chaque passager peut avoir un ou plusieurs bagages. Les informations sur les bagages peuvent inclure le poids, les dimensions, et le type de bagage (bagage à main, bagage enregistré).
18. Service de vol : Sur chaque vol, différents services peuvent être proposés tels que des repas, des divertissements en vol, du Wi-Fi, etc.
19. Personnel de bord : Chaque vol a un équipage, qui comprend des pilotes et des membres d'équipage de cabine.
20. Maintenance : Chaque avion nécessite une maintenance régulière. Les détails de la maintenance pourraient inclure la date de la dernière maintenance, le type de maintenance effectuée, et l'état actuel de la maintenance (nécessaire, en cours, terminée).
21. Suivi en temps réel : Pendant un vol, des informations en temps réel sont disponibles, comme la localisation actuelle de l'avion, l'heure d'arrivée prévue, et d'autres mises à jour de vol.
22. Commentaires/Réclamations : Les passagers ont la possibilité de laisser des commentaires sur leurs vols ou de faire des réclamations. Cela pourrait inclure une description du problème, la date, le vol concerné, et le statut de la réclamation (en attente, résolu).

# SMART TASKS

# Tasks :

1. Configurer l'environnement de développement et les bibliothèques Python nécessaires (1 jour)
2. Créer une structure de projet en Python (1 jour)
3. Implémenter une fichier JSON pour stocker les informations (1 jour)
4. faire un script pour simuler le mouvement d'un avion (2 jours)
5. Adapter l'interface utilisateur pour les administrateurs afin qu'ils puissent réserver des avions marchand (2 jours)
6. Ajouter des paramètres de contrôle de vol (vitesse, altitude, direction) (1jour)
7. Implémenter un algorithme de simulation de la météo (vent, température) (2 jour)
8. implementer un simulation de paiement pour la réservation de ticket (1 jour)
9. Intégrer des éléments graphiques pour représenter les avions et le paysage  y compris le décollage (5 jours) 
10. Créer une fonction pour générer des aéroports avec des noms et des codes uniques (1 jour)
11. Implémenter un système de recherche d'aéroports par code (1 jour)
12. Créer un système de gestion des vols, y compris les horaires et les routes (4 jours)
13. Ajouter une fonction pour vérifier la disponibilité des vols (2 jours)
14. Développer un formulaire de réservation de billets (2 jours)
15. Implémenter la validation des données du formulaire de réservation (2 jours)
16. Créer un système pour générer des numéros de billets uniques (1 jour)
17. Ajouter une fonction pour afficher les détails du billet après la réservation (1 jour)
18. Stocker les informations des avions de ligne et des avions marchand (1 jour)
19. Créer une fonction pour ajouter de nouveaux avions de ligne et avions marchand  (2 jours)
20. Implémenter une fonction pour lire et rechercher des avions de ligne et avions marchand (2 jours)
21. Inclure le type d'avion (avions de ligne ou avions marchand) (1 jour)
22. Créez une interface utilisateur pour permettre aux administrateurs de créer et gérer les avions de ligne et les avions marchand (3 jours)
23. Modifier l'interface utilisateur de réservation pour les utilisateurs afin d'inclure uniquement les avions de ligne (2 jours)
24. Créer une fonction pour attribuer les places disponibles lors de la réservation d'un billet en fonction du type d'avion (2 jours).
25. Ajouter une vérification du poids des bagages des utilisateurs lors de la réservation d'un billet. Si le poids total des bagages dépasse le poids maximum autorisé pour l'avion, refusez la réservation et informez l'utilisateur (2 jours).
26. Modifier le formulaire de réservation pour inclure une entrée du poids des bagages et une sélection de sièges (2 jours).
27. Metter à jour l'interface utilisateur pour afficher les places et le poids maximum autorisés pour chaque avion lors de la recherche de vols (2 jours).
28. Afficher un avertissement aux utilisateurs lors de la réservation si le poids de leurs bagages dépasse le poids maximum autorisé pour l'avion sélectionné (1 jour).
29. Implémenter un mécanisme pour empêcher les utilisateurs de réserver plus de sièges que le nombre de places disponibles dans un avion (2 jours).
30. Mettre à jour l'interface utilisateur pour les administrateurs afin de leur permettre de définir et de modifier le nombre de places et le poids maximum autorisés pour chaque type d'avion (2 jours).
31. Créer un système de connexion pour les utilisateurs (2 jours)
32. envoie de mail avec les informations de connexions (1 jour)
33. Implémenter un système de gestion des comptes utilisateurs (3 jours)
34. Ajouter la possibilité de modifier les informations de compte (1 jour)
35. Créer une fonction de récupération de mot de passe (1jour)
36. Implémenter un système de connexion pour les administrateurs (1 jour)
37. Créer un système de gestion des vols pour les administrateurs (3 jours)
38. Ajouter la possibilité de modifier les horaires et les routes des vols (2 jours)
39. Implémenter un système de gestion des aéroports pour les administrateurs (2 jours)
40. Créer une fonction pour ajouter, modifier ou supprimer des aéroports (2 jours)
41. Implémenter un système de gestion des utilisateurs pour les administrateurs (2 jours)
42. Ajouter la possibilité de bloquer ou débloquer des comptes utilisateurs (1 jour)
43. Créer un système de gestion des réservations pour les administrateurs (2 jours)
44. Ajouter la possibilité d'annuler ou de modifier des réservations (2 jours)
45. Implémenter un système de reporting pour les administrateurs (3 jours)
46. Créer des rapports sur les vols, les réservations et les revenus (matplot) (3 jours)
47. Créez une interface utilisateur pour la gestion des réservations par les administrateurs (2 jours)
48. Ajouter des contrôles pour annuler ou modifier des réservations (2 jours)
49. Implémenter une interface utilisateur pour le système de reporting (2 jours)
50. Créer des contrôles pour générer et afficher des rapports (2 jours)
51. Tester l'ensemble des fonctionnalités du simulateur de vol (4 jours)
52. Tester le système de réservation de billets (3 jours)
53. Tester le système de connexion pour les utilisateurs et les administrateurs (2 jours)
54. Tester le système de gestion des comptes utilisateurs et administrateurs (3 jours)
55. Tester le système de gestion des vols et des aéroports (3 jours)
56. Tester le système de gestion des réservations et des rapports (3 jours)
57. Tester l'interface utilisateur du simulateur de vol (2 jours)
58. Tester l'interface utilisateur du système de réservation (2 jours)
59. Tester l'interface utilisateur du système de connexion (1 jour)
60. Tester l'interface utilisateur du système de gestion des comptes (2 jours)
61. Tester l'interface utilisateur du système de gestion des vols et des aéroports (2 jours)
62. Tester l'interface utilisateur du système de gestion des réservations et des rapports (2 jours)
63. Identifiez et documentez les problèmes et les erreurs (2 jours)
64. Corriger les problèmes et les erreurs identifiés (5 jours)
65. Réaliser des tests supplémentaires après correction (2 jours)
66. Améliorer l'interface utilisateur et l'expérience utilisateur (4 jours)
67. Préparer des scénarios de tests pour la démonstration du projet (2 jours)
68. Préparer une présentation pour expliquer les fonctionnalités et les choix techniques (2 jours)

# Bonus :

1. Récompenses et classements : Implémentez un système de récompenses pour les utilisateurs qui réservent fréquemment des billets ou qui volent souvent sur des avions de ligne. Vous pourriez également créer un classement des utilisateurs en fonction des miles parcourus.
2. Notifications en temps réel : Envoyez des notifications en temps réel aux utilisateurs pour les informer des changements de vol, des retards ou des annulations.
3. Planificateur d'itinéraire : Créez une fonctionnalité permettant aux utilisateurs de planifier leurs itinéraires en choisissant plusieurs vols pour atteindre leur destination finale.
4. Chat en direct : Intégrez un chat en direct pour permettre aux utilisateurs de discuter avec les administrateurs ou d'autres utilisateurs en cas de besoin.
5. Système de recommandation : Développez un algorithme pour recommander des vols, des destinations et des offres spéciales aux utilisateurs en fonction de leurs préférences et de leur historique de réservation.

# Libraries :

- Tkinter ou PyQt : Ces bibliothèques sont utilisées pour créer des interfaces graphiques en Python. Tkinter est inclus avec la plupart des installations Python, tandis que PyQt offre des fonctionnalités plus avancées et une apparence plus moderne.
- Beautiful Soup : Utilisez cette bibliothèque pour analyser et extraire des données à partir de documents HTML ou XML, par exemple pour récupérer des informations sur les vols à partir de sites Web de compagnies aériennes.
- Pandas : Cette bibliothèque est utile pour manipuler et analyser des données structurées. Vous pouvez l'utiliser pour filtrer, trier et manipuler les données sur les vols et les réservations.
- NumPy : Cette bibliothèque est utilisée pour les calculs numériques et peut être utile pour les calculs liés à la simulation de vol.
- Matplotlib ou Plotly : Utilisez ces bibliothèques pour créer des graphiques et des visualisations interactives, par exemple pour afficher les statistiques sur les vols et les réservations.
- PyOWM ou OpenWeatherMap : Ces bibliothèques facilitent l'accès aux données météorologiques pour intégrer des conditions météorologiques réalistes dans votre simulateur de vol.
- Geopy : Cette bibliothèque facilite le calcul des distances et la manipulation des coordonnées géographiques, ce qui peut être utile pour calculer les distances entre les aéroports et déterminer les temps de vol.
- APScheduler : Utilisez cette bibliothèque pour planifier des tâches à exécuter périodiquement, par exemple pour mettre à jour les informations météorologiques ou les données sur le trafic aérien.
- SQLAlchemy : cette bibliothèque ORM (Object-Relational Mapping) peut être utilisée pour interagir avec des fichiers JSON de manière plus structurée et similaire à une base de données.
- Pillow : Cette bibliothèque est utilisée pour manipuler des images en Python et peut être utile pour traiter et afficher des images d'avions, d'aéroports ou de destinations.
- Scikit-learn : Si vous souhaitez implémenter un système de recommandation basé sur l'apprentissage automatique, Scikit-learn est une bibliothèque d'apprentissage automatique qui peut vous aider à construire et entraîner des modèles de recommandation.
- Arrow ou Pendulum : Ces bibliothèques facilitent la manipulation des dates et des heures en Python et peuvent être utiles pour gérer les horaires des vols et les fuseaux horaires.
- Twilio ou SendGrid : Utilisez ces bibliothèques pour envoyer des notifications par SMS ou par e-mail aux utilisateurs concernant leurs vols, leurs réservations et les mises à jour importantes.
- waze route calculator : permet de calculer la disctance entre 2 itinéraires

# Entités 

1. **`User`** :
        - id
        - nom
        - email
        - mot de passe
        - rôle
        - réservations
3. **`Aircraft`** :
    - id
    - modèle
    - capacité
    - status
4. **`PassengerAircraft`** : hérite de **`Aircraft`**
    - numéro de siège
5. **`CargoAircraft`** : hérite de **`Aircraft`**
    - capacité de charge
6. **`Airport`** :
    - id
    - nom
    - lieu
    - pistes
    - avions disponibles
7. **`Flight`** :
    - id
    - aéroport de départ
    - aéroport d'arrivée
    - heure de départ
    - heure d'arrivée
    - avion
    - itinéraire
    - passagers
8. **`Booking`** :
    - id
    - utilisateur
    - vol
    - date de réservation
9. **`Itinerary`** :
    - id
    - vol
    - heure de départ
    - heure d'arrivée
    - aéroport de départ
    - aéroport d'arrivée

# Relations 

1. **`User`**:
    - a de nombreuses **`Booking`** (un utilisateur peut faire de nombreuses réservations)
2. **`Admin`** et **`Passenger`** héritent de **`User`** :
    - **`Admin`** peut gérer **`Aircraft`** et **`Airport`**
    - **`Passenger`** peut avoir de nombreuses **`Booking`**
3. **`Aircraft`** :
    - est associé à de nombreux **`Flight`** (un avion peut être utilisé pour de nombreux vols)
4. **`PassengerAircraft`** et **`CargoAircraft`** héritent de **`Aircraft`** :
    - Ils ont leurs propres attributs spécifiques
5. **`Airport`** :
    - a de nombreux **`Aircraft`** disponibles (plusieurs avions peuvent être stationnés dans un aéroport)
    - est associé à de nombreux **`Flight`** à travers les aéroports de départ et d'arrivée
6. **`Flight`** :
    - est associé à un **`Aircraft`** (un vol utilise un avion spécifique)
    - a un **`Airport`** de départ et un **`Airport`** d'arrivée
    - a un **`Itinerary`**
    - a de nombreux **`Passenger`** via **`Booking`** (plusieurs passagers peuvent être sur un vol)
7. **`Booking`** :
    - est associé à un **`User`** (une réservation est faite par un utilisateur)
    - est associé à un **`Flight`** (une réservation concerne un vol spécifique)
8. **`Itinerary`** :
    - est associé à un **`Flight`** (un itinéraire concerne un vol spécifique)