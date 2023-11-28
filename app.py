from flask import Flask, render_template, request, redirect, url_for, flash, Request

app = Flask(__name__)

#Object article
class Article:
    def __init__(self,id, title, content, author, date, intro, category, illustration):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.note = 1
        self.intro = intro
        self.category = category
        self.illustration = illustration

#List of articles
articles_list = [
    Article(1,'Comment Prévenir les Obstructions dans Vos Toilettes ?',
             {
                 "1. Utilisez du papier toilette de qualité": "Le papier toilette de qualité est plus épais et plus résistant que le papier toilette ordinaire. Il est également plus doux et plus confortable à utiliser. Le papier toilette de qualité est moins susceptible de se déchirer et de se coincer dans les tuyaux, ce qui peut entraîner des obstructions. Il est également moins susceptible de se décomposer lorsqu'il est mouillé, ce qui peut entraîner des obstructions dans les toilettes. Le papier toilette de qualité est plus cher que le papier toilette ordinaire, mais il peut vous faire économiser de l'argent à long terme en réduisant le risque d'obstructions dans les toilettes.",
                    "2. Ne jetez pas de produits hygiéniques dans les toilettes": "Les produits d'hygiène féminine, comme les tampons et les serviettes hygiéniques, ne se décomposent pas dans l'eau. Ils peuvent donc se coincer dans les tuyaux et provoquer des obstructions. Jetez toujours les produits d'hygiène féminine dans une poubelle et non dans les toilettes.",
                    "3. Ne jetez pas de lingettes humides dans les toilettes": "Les lingettes humides ne se décomposent pas dans l'eau et peuvent donc se coincer dans les tuyaux et provoquer des obstructions. Jetez toujours les lingettes humides dans une poubelle et non dans les toilettes.",
                    "4. Ne jetez pas de couches dans les toilettes": "Les couches ne se décomposent pas dans l'eau et peuvent donc se coincer dans les tuyaux et provoquer des obstructions. Jetez toujours les couches dans une poubelle et non dans les toilettes.",
                    "5. Ne jetez pas de cheveux dans les toilettes": "Les cheveux ne se décomposent pas dans l'eau et peuvent donc se coincer dans les tuyaux et provoquer des obstructions. Jetez toujours les cheveux dans une poubelle et non dans les toilettes.",
                    "6. Ne jetez pas de coton dans les toilettes": "Le coton ne se décompose pas dans l'eau et peut donc se coincer dans les tuyaux et provoquer des obstructions. Jetez toujours le coton dans une poubelle et non dans les toilettes.",
                    "7. Entretenez vos canalisations régulièrement:": "Les obstructions dans les toilettes peuvent être causées par des tuyaux bouchés. Pour éviter les obstructions, faites inspecter et nettoyer vos canalisations régulièrement par un plombier professionnel.",
                    "8. Utilisez un filtre à cheveux dans la baignoire": "Les cheveux peuvent s'accumuler dans les tuyaux de la baignoire et provoquer des obstructions. Pour éviter les obstructions, utilisez un filtre à cheveux dans la baignoire.",
                    "9. Enseignez aux enfants les bonnes pratiques d'utilisation des toilettes": "Les enfants peuvent jeter des objets dans les toilettes, ce qui peut provoquer des obstructions. Pour éviter les obstructions, enseignez aux enfants les bonnes pratiques d'utilisation des toilettes.",

             }, 
             'Hean Le villageois', 
             "Aujourd'hui",
             "Les obstructions de toilettes peuvent être des inconvénients gênants, mais il existe des mesures simples que vous pouvez prendre pour prévenir ces problèmes courants de plomberie. Suivez ces conseils pratiques pour maintenir un système de plomberie sans souci.",
             "Plomberie",
             "fond2.jpg"
            ),
    Article(2,
        "Les Signes d'un Problème de Plomberie Imminent dans Votre Maison", 
        {
            "1. Bruits étranges dans la canalisation":"Des bruits de gargouillement, de claquement ou de grondement dans les canalisations peuvent indiquer des obstructions ou des problèmes de pression d'eau. Ne négligez pas ces sons et envisagez une inspection professionnelle pour identifier la cause sous-jacente.",
            "2. Odeurs d'égout":"Les odeurs d'égout peuvent indiquer un problème de plomberie sous-jacent. Si vous sentez des odeurs d'égout dans votre maison, faites inspecter vos canalisations par un plombier professionnel.",
            "3. Faible pression d'eau":"Une faible pression d'eau peut être causée par des obstructions dans les canalisations ou des fuites dans les tuyaux. Si vous avez une faible pression d'eau dans votre maison, faites inspecter vos canalisations par un plombier professionnel.",
            "4. Fuites d'eau":"Les fuites d'eau peuvent être causées par des tuyaux cassés ou des joints desserrés. Si vous avez des fuites d'eau dans votre maison, faites inspecter vos canalisations par un plombier professionnel.",
            "5. Taches d'eau sur les murs ou les plafonds":"Les taches d'eau sur les murs ou les plafonds peuvent être causées par des fuites dans les tuyaux. Si vous avez des taches d'eau sur les murs ou les plafonds de votre maison, faites inspecter vos canalisations par un plombier professionnel."
        }, 
        'Hean Le villageois', 
        'Hier',
        "Les problèmes de plomberie peuvent être coûteux et désagréables. Il est important de reconnaître les signes d'un problème de plomberie imminent dans votre maison afin de pouvoir prendre des mesures pour les résoudre avant qu'ils ne deviennent des problèmes majeurs.",
        "Débouchage",
        "problem.jpg"
    ),
    Article(3,
        "Les avantages de l'inspection par Caméra pour les canalisations",
        {
            "1. Localisation précise des problèmes":"L'inspection par caméra permet une visualisation en temps réel de l'intérieur de vos canalisations. Cela signifie que les techniciens peuvent localiser précisément l'endroit exact où se trouve le problème, que ce soit une obstruction, une fissure ou une autre anomalie.",
            "2. Diagnostic rapide et efficace": "Contrairement aux méthodes traditionnelles qui peuvent nécessiter des essais et erreurs, l'inspection par caméra permet un diagnostic rapide. Les techniciens peuvent identifier rapidement la cause du problème, ce qui se traduit par des réparations plus rapides et moins invasives.",
            "3. Economies de temps et d'argent": "En réduisant le temps nécessaire pour identifier et résoudre un problème, l'inspection par caméra permet des économies significatives. Moins de temps d'intervention signifie également moins d'inconfort pour les occupants de la maison et une reprise plus rapide de l'utilisation normale des installations.",
            "4. Prévention des problèmes futurs": "L'inspection par caméra n'est pas seulement utile pour résoudre les problèmes existants, elle peut également être utilisée à des fins préventives. En identifiant les signes avant-coureurs de problèmes potentiels, vous pouvez prendre des mesures correctives avant qu'ils ne deviennent des situations critiques.",
            "5. Documentation visuelle pour les clients": "L'inspection par caméra offre la possibilité de fournir une documentation visuelle aux clients. Cela permet de renforcer la transparence et la confiance en montrant clairement les problèmes détectés et les réparations effectuées. C'est également un outil pédagogique précieux pour sensibiliser les clients à l'état de leurs canalisations."
        },
        'Hean Le villageois',
        '23 octobre',
        "L'inspection par caméra est devenue une méthode inestimable pour diagnostiquer les problèmes de plomberie de manière précise et efficace. Découvrez les avantages de cette technologie moderne pour assurer la santé de vos canalisations.",
        "Inspection",
        "camera.jpg"
        ),
    
    Article(4,
            "Top 10 Erreurs à Eviter en cas de toilettes bouchées",
            {
                "1. Utiliser des produits chimiques agressifs":"Bien que les produits chimiques de débouchage soient largement disponibles, leur utilisation excessive peut endommager vos canalisations. Optez plutôt pour des solutions naturelles ou faites appel à des professionnels pour un débouchage sûr.",
                "2. Utiliser des objets pointus ou métalliques":"Insérer des objets pointus ou métalliques dans la cuvette pour déloger l'obstruction peut entraîner des éraflures, des fissures ou même des dégâts plus graves aux canalisations. Privilégiez des outils spécifiquement conçus pour le débouchage.",
                "3. Trop tirer la chasse d'eau":"Répétitivement tirer la chasse d'eau en cas de blocage peut causer un débordement et des dégâts d'eau. Au lieu de cela, attendez que l'eau se calme et évaluez la situation avant d'agir.",
                "4. Ignorer les signes précurseurs":"Les toilettes qui se vident lentement ou font des bruits étranges sont des signes de problèmes imminents. Ignorer ces signaux peut conduire à des obstructions plus graves. Agissez dès que vous remarquez des changements inhabituels.",
                "5. Utiliser des objets inappropriés pour le débouchage":"Évitez d'utiliser des objets durs tels que des cintres métalliques, qui peuvent endommager le revêtement de la cuvette. Privilégiez des ventouses ou des outils spécialement conçus pour les toilettes.",
                "6. Verser des produits corrosifs":"Les produits chimiques corrosifs peuvent endommager les composants internes de la toilette et causer des problèmes plus graves. Utilisez des solutions plus douces et recherchez des alternatives respectueuses de l'environnement.",
                "7. Démonter la toilette sans expérience":"Démonter la toilette sans connaissances préalables peut entraîner des problèmes supplémentaires. Si vous ne vous sentez pas à l'aise, il est préférable de faire appel à un professionnel pour éviter d'aggraver la situation.",
                "8. Reporter l'intervention professionnelle" :"Si les solutions domestiques échouent, ne tardez pas à faire appel à des professionnels. Reporter une intervention peut aggraver les obstructions et causer des dommages coûteux.",
                "9. Utiliser des quantités excessives de papier toilette":"Une utilisation excessive de papier toilette est l'une des principales causes de blocage. Limitez la quantité utilisée et encouragez les membres de votre foyer à adopter des habitudes d'utilisation plus responsables.",
                "10. Négliger l'entretien préventif":"Prévenir les obstructions nécessite un entretien régulier. Optez pour un entretien préventif, y compris l'utilisation de produits adaptés, pour éviter les problèmes à long terme."  
                },
            'Hean Le villageois',
            '20 octobre',
            "Les toilettes bouchées peuvent être une source de stress, mais agir précipitamment peut parfois aggraver la situation. Voici les dix erreurs les plus courantes à éviter lorsque vous êtes confronté à des toilettes bouchées.",
            "Débouchage",
            "wc.jpg"
        ),
    Article(5,
            "Les Différences entre les Produits de Débouchage Chimiques et les Méthodes Naturelles",
            {
                "Les produits de Débouchage Chimiques : " : "Avantages : ; 1. Rapidité d'action : Les produits chimiques agissent généralement rapidement pour décomposer les obstructions, offrant une solution immédiate. | 2. Disponibilité : Facilement accessibles dans les magasins, ces produits sont souvent la première option pour de nombreux consommateurs en cas de problème de plomberie. | 3. Efficacité sur les obstructions sévères : Les produits chimiques peuvent être efficaces pour traiter des obstructions plus graves dans les canalisations. ; Inconvénients : | 1. Toxicité : La plupart des produits chimiques de débouchage sont toxiques et peuvent présenter des risques pour la santé humaine et l'environnement. | 2. Endommagement des canalisations : L'utilisation fréquente de produits chimiques agressifs peut endommager les canalisations au fil du temps, provoquant des fuites et des ruptures. | 3. Inefficacité sur certains types d'obstructions : Certains types d'obstructions, comme les accumulations de cheveux ou les objets solides, peuvent résister aux produits chimiques.",
                "Les Methodes Naturelles : " : "Avantages : | 1. Non toxique : Les méthodes naturelles sont non toxiques et ne présentent aucun risque pour la santé humaine ou l'environnement. | 2. Non corrosif : Les méthodes naturelles sont non corrosives et n'endommagent pas les canalisations. | 3. Efficacité sur certains types d'obstructions : Les méthodes naturelles peuvent être efficaces pour traiter certains types d'obstructions, comme les accumulations de cheveux ou les objets solides. ; Inconvénients : | 1. Lenteur d'action : Les méthodes naturelles peuvent prendre plus de temps pour décomposer les obstructions, ce qui peut être un inconvénient pour les obstructions sévères. | 2. Disponibilité : Les méthodes naturelles ne sont pas toujours facilement disponibles dans les magasins, ce qui peut être un inconvénient pour les consommateurs qui recherchent une solution rapide. | 3. Efficacité sur les obstructions sévères : Les méthodes naturelles peuvent ne pas être efficaces pour traiter les obstructions sévères dans les canalisations.",
                "Conclusion : " : "En conclusion, le choix entre les produits de débouchage chimiques et les méthodes naturelles dépend de plusieurs facteurs, y compris la gravité de l'obstruction, l'impact sur l'environnement, et votre préférence personnelle. Il est toujours judicieux d'opter pour des méthodes naturelles lorsque cela est possible, favorisant ainsi une approche plus durable et respectueuse de l'environnement."

            },
            'Hean Le villageois',
            '18 octobre',
            "Lorsqu'il s'agit de déboucher des canalisations, de nombreuses options s'offrent à vous. Cependant, il est crucial de comprendre les différences entre les produits de débouchage chimiques et les méthodes naturelles. Choisir la bonne approche peut faire la différence entre une solution efficace et des problèmes persistants.",
            "Entretien",
            "entretien.jpg"
        )

]


@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html', articles=articles_list[-3:])

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=articles_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article/<id>')
def article(id):
    return render_template('article.html', article=next(filter(lambda x: x.id == int(id), articles_list), None))

if __name__ == '__main__':
    app.run(host="0.0.0.0")