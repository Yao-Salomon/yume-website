/*
    Ce script est une implémentation de l'objet xhr permettant de gérer un module de recherche
    qui comprend les options de recherches suivantes: le nom, le prix,le nombre d'étoiles, le lieu de livraison, et le fournisseur)
    Ces options seront fournies comme des filtres de recherche(cochée ou décochée)
    
    yume ajax version 1.0.0

*/

function loadFile(text) {

    /*
        Déclaration des variables globales
            + création de l'objet xhr
            + initialisation de la source de données
            + regex utilisé pour les tests sur le fichier json

    */

    var xhr = new XMLHttpRequest();
    var xhr2 = new XMLHttpRequest();
    var xhr3 = new XMLHttpRequest();

    var lien_produits="http://localhost:8000/yume-api/produits/?format=json"
    var lien_fonctionalites="http://localhost:8000/yume-api/fonctionalites/?format=json"
    var lien_blog="http://localhost:8000/yume-api/blog/?format=json"

    let regexe=new RegExp('(.*)('+text+')(.*)','i')

    //ouverture de la source json
    xhr.open("GET",lien_produits)
    xhr2.open("GET",lien_fonctionalites)
    xhr3.open("GET",lien_blog)

    //test de statut de la requête ajax
    xhr.onreadystatechange = function() {  
        xhr2.onreadystatechange=function(){
            xhr3.onreadystatechange=function(){

                if (xhr.readyState == 4 && xhr.status == 200 && xhr2.readyState == 4 && xhr2.status == 200 && xhr3.readyState == 4 && xhr3.status == 200) {
            
    
                    produits=JSON.parse(xhr.responseText);
                    fonctionalites=JSON.parse(xhr2.responseText);
                    blog=JSON.parse(xhr3.responseText);
                    
                    let result=[];
                    let test=false;
        
        
                    for (el in produits){
                        if(regexe.test(produits[el].nom)){
                            test=true
                            result.push(produits[el].nom.replace(regexe,'<a href="" class="btn btn-annuaire-primary m-1"><i class="bi-'+produits[el].icon+' me-1"></i> $1<span class="fw-bolder">$2</span>$3</a>'))                            
                        }
                    }
    
                    for(el in fonctionalites){
                        
                        if(regexe.test(fonctionalites[el].nom)){
                            test=true
                            result.push(fonctionalites[el].nom.replace(regexe,'<a href="" class="btn btn-warning m-1"><i class="bi-'+fonctionalites[el].icon+' me-1"></i> $1<span class="fw-bolder">$2</span>$3</a>'))                            
                        }
                    }

                    for(el in blog){
                        
                        if(regexe.test(blog[el].titre)){
                            test=true
                            result.push(blog[el].titre.replace(regexe,'<a href="http://localhost:8000/blog/'+blog[el].slug+' " class="btn btn-primary m-1"><i class="bi-'+blog[el].icon+' me-1"></i> $1<span class="fw-bolder">$2</span>$3</a>'))                            
                        }
                    }

                    result=result.splice(0,10)
                    document.getElementById("texte").innerHTML=test?"":"<p class='fw-bolder text-center text-white'>Aucun résultat</p>"
                    
                    result.forEach(function(element){
                        document.getElementById("texte").innerHTML+=test?element:"<p class='fw-bolder text-white text-center'> Aucun résultat</p>"
                    })
                    
        
                }else if(xhr.readyState == 4 && xhr.status != 200&& xhr2.readyState == 4 && xhr2.status == 200 && xhr3.readyState == 4 && xhr3.status == 200) {
                    
                    document.getElementById("texte").innerHTML="<span class='fw-bolder'>Aucun résultat Erreur"+ xhr.status + '\nTexte : ' + xhr.statusText+"</span>"
        
                }
            }
            
        }
        //test de l'état de la requête
    }
    
    xhr.send(null); 
    xhr2.send(null);
    xhr3.send(null);
}

//fonction anonyme permettant l'initialisation de la requête ajax

(function() {
    
    searchbar_sm=document.getElementById("search_sm");
    searchbar_md=document.getElementById("search_md");

    searchbar_sm.addEventListener("keyup",function(e){
        if(searchbar_sm.value!=''&& searchbar_sm.value!=' '){
            loadFile(searchbar_sm.value)
        }
    },true)

    searchbar_md.addEventListener("keyup",function(e){
        if(searchbar_md.value!=''&& searchbar_md.value!=' '){
            loadFile(searchbar_md.value)
        }
    },true)
    
    
})();