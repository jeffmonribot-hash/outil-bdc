# Outil BDC – Architecture du projet

## 🎯 Objectif
Prototype d’un outil métier simple pour la gestion des Bons de Commande (BDC).
Objectif : remplacer / compléter des fichiers Excel par un outil plus robuste,
évolutif et simple d’utilisation.

---

## 🧭 Vision globale
Le logiciel est organisé autour de :
- une interface graphique (écrans)
- des données structurées (BDC, sites, tiers)
- des actions métier (enregistrer, consulter, suivre)

---

## 🖥️ Écrans prévus

### 1. Écran principal – Liste des BDC
- Affichage de tous les BDC
- Boutons :
  - Nouveau BDC
  - Modifier (plus tard)
  - Supprimer (plus tard)

### 2. Écran Nouveau BDC
- Champs :
  - Site
  - Tiers
  - Objet
  - Montant
- Bouton :
  - Enregistrer

---

## 🗄️ Données

### BDC
- site
- tiers
- objet
- montant
- statut (prévu)

### Référentiels (à importer)
- Sites
- Tiers
- Agents (plus tard)

---

## 🔄 Interactions principales

- Bouton "Nouveau BDC"
  → ouverture de l’écran Nouveau BDC

- Bouton "Enregistrer"
  → création d’un BDC
  → retour à l’écran principal
  → affichage dans la liste

---

## 🟢 État d’avancement

- Prototype visuel : 🟢 OK
- Saisie BDC : 🟢 OK
- Données structurées : 🟢 OK
- Sauvegarde disque : 🟡 À faire
- Référentiels importés : 🔴 À faire
- Connexion mail / Outlook : 🔴 À faire

