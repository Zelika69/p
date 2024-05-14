function suma() 
        {
            var x, y, text, suma;
            x = document.getElementById("numero1").value;
            y = document.getElementById("numero2").value;
            if (isNaN(x) || isNaN(y)) {
                text = "Ingrese un numero valido en las inputs";
            }else{
                suma = parseFloat(x) + parseFloat(y);
                text = suma;
            }
            
            document.getElementById("resultado").innerHTML = text;
        }