#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 DevicePilot Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from common.utils import hashIt

female_names=["Amelia","Olivia","Isla","Emily","Poppy","Ava","Isabella","Jessica","Lily","Sophie","Grace","Sophia","Mia","Evie","Ruby","Ella","Scarlett","Isabelle","Chloe","Sienna","Freya","Phoebe","Charlotte","Daisy","Alice","Florence","Eva","Sofia","Millie","Lucy","Evelyn","Elsie","Rosie","Imogen","Lola","Matilda","Elizabeth","Layla","Holly","Lilly","Molly","Erin","Ellie","Maisie","Maya","Abigail","Eliza","Georgia","Jasmine","Esme","Willow","Bella","Annabelle","Ivy","Amber","Emilia","Emma","Summer","Hannah","Eleanor","Harriet","Rose","Amelie","Lexi","Megan","Gracie","Zara","Lacey","Martha","Anna","Violet","Darcey","Maria","Maryam","Brooke","Aisha","Katie","Leah","Thea","Darcie","Hollie","Amy","Mollie","Heidi","Lottie","Bethany","Francesca","Faith","Harper","Nancy","Beatrice","Isabel","Darcy","Lydia","Sarah","Sara","Julia","Victoria","Zoe","Robyn"]

male_names=["Oliver","Jack","Harry","Jacob","Charlie","Thomas","George","Oscar","James","William","Noah","Alfie","Joshua","Muhammad","Henry","Leo","Archie","Ethan","Joseph","Freddie","Samuel","Alexander","Logan","Daniel","Isaac","Max","Mohammed","Benjamin","Mason","Lucas","Edward","Harrison","Jake","Dylan","Riley","Finley","Theo","Sebastian","Adam","Zachary","Arthur","Toby","Jayden","Luke","Harley","Lewis","Tyler","Harvey","Matthew","David","Reuben","Michael","Elijah","Kian","Tommy","Mohammad","Blake","Luca","Theodore","Stanley","Jenson","Nathan","Charles","Frankie","Jude","Teddy","Louie","Louis","Ryan","Hugo","Bobby","Elliott","Dexter","Ollie","Alex","Liam","Kai","Gabriel","Connor","Aaron","Frederick","Callum","Elliot","Albert","Leon","Ronnie","Rory","Jamie","Austin","Seth","Ibrahim","Owen","Caleb","Ellis","Sonny","Robert","Joey","Felix","Finlay","Jackson"]

last_names = ["Adams","Aigner","Allen","Andersen","Anderson","Andr??","Andreassen","Angelopoulos","Antoniou","Athanasiadis","Auer","Babi??","Bailey","Baker","Bakker","Barbieri","Bari??i??","Barnes","Bauer","Baumgartner","Becker","Bell","Bennett","Berg","Berger","Bernard","Bertrand","Bianchi","Binder","Bla??evi??","Bogdanov","Bonnet","Bos","Bo??njak","Bo??i??","Brooks","Brouwer","Brown","Brunner","Bruno","Butler","Campbell","Carter","Caruso","Christensen","Christiansen","Claes","Clark","Clarke","Collins","Colombo","Conti","Cook","Cooper","Costa","Cox","Cruz","Dahl","David","Davies","Davis","De Boer","De Graaf","De Groot","De Jong","De Luca","De Smet","De Vries","De Wit","Dekker","Diaz","Dijkstra","Dimitriadis","Dubois","Dubois","Dupont","Durand","Ebner","Eder","Edwards","Egger","Eriksen","Esposito","Evans","Ferrari","Filipovi??","Fischer","Fisher","Flores","Fontana","Foster","Fournier","Fran??ois","Fuchs","Gallo","Garcia","Garcia","Georgiou","Giordano","Girard","Golubev","Gomez","Gonzalez","Goossens","Gray","Greco","Green","Grgi??","Gruber","Gutierrez","Haas","Hagen","Hall","Halvorsen","Hansen","Harris","Haugen","Heilig","Hendriks","Henriksen","Hernandez","Hill","Hofer","Hoffmann","Horvat","Howard","Huber","Hughes","Ivanov","Jackson","Jacobs","Jacobsen","James","Jansen","Janssen","Janssens","Jenkins","Jensen","Johannessen","Johansen","Johnsen","Johnson","Jones","J??rgensen","Juki??","Juri??","Karlsen","Kelly","King","Kne??evi??","Koller","Kova??","Kova??evi??","Kova??i??","Kozlov","Kristiansen","Kuznetsov","Lambert","Lang","Larsen","Laurent","Lebedev","Lechner","Lee","Lefebvre","Lef??vre","Lehner","Leitner","Leroy","Lewis","Lombardi","Long","Lopez","Lovri??","Lund","Madsen","Maes","Maier","Mancini","Mariani","Mari??","Marino","Markovi??","Martin","Martinez","Martinez","Mati??","Mayer","Mayr","Meijer","Meyer","Mercier","Mertens","Meyer","Michel","Miller","Mitchell","M??ller","Moore","Morales","Moreau","Morel","Moretti","Morgan","Morozov","Morris","Mortensen","Moser","Mulder","M??ller","Murphy","Myers","Nelson","Nguyen","Nielsen","Nikolaidis","Nilsen","Novak","Novikov","Olsen","Ortiz","Panagiotopoulos","Papadakis","Papadopoulos","Papantoniou","Parker","Pavi??","Pavlov","Pavlovi??","Pedersen","Peeters","Perez","Peri??","Perkovi??","Perry","Peters","Petersen","Peterson","Petit","Petridis","Petrov","Petrovi??","Pettersen","Phillips","Pichler","Popov","Popovi??","Poulsen","Powell","Price","Radi??","Ramirez","Rasmussen","Reed","Reiter","Reyes","Ricci","Richard","Richardson","Rinaldi","Rivera","Rizzo","Robert","Roberts","Robinson","Rodriguez","Rogers","Romano","Ross","Rossi","Roux","Russell","Russo","Sanchez","Sanders","Santoro","??ari??","Schmid","Schmidt","Schneider","Schulz","Schuster","Schwarz","Scott","Semyonov","Simon","Simon","Smirnov","Smit","Smith","Smits","Sokolov","Solovyov","S??rensen","Steiner","Stewart","Sullivan","Taylor","Thomas","Thompson","Thomsen","Tomi??","Torres","Turner","Van den Berg","Van der Meer","Van Dijk","Van Leeuwen","Vasilyev","Vidovi??","Vincent","Vinogradov","Visser","Vlahos","Volkov","Vorobyov","Vos","Vukovi??","Wagner","Walker","Wallner","Ward","Watson","Weber","White","Willems","Williams","Wilson","Wimmer","Winkler","Wolf","Wood","Wouters","Wright","Young","Zaytsev"]

def first_name(r):
    if hashIt(r,1):
        first = female_names
    else:
        first = male_names
    return first[hashIt(r,len(first))]

def last_name(r):
    return last_names[hashIt(r,len(last_names))]

def full_name(r):
    return first_name(r) + " " + last_name(r)
