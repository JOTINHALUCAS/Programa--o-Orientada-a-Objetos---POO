// Identificar o tipo de geometria a partir de 4 coordenadas inseridas pelo usuário,
//  seja quadrado ou retângulo;

// Que Deus abençõe o meus estudos , amém

// DOM Utilizando

function quad_ret(){
    var x1_str = window.document.getElementById('x1')
    var y1_str = window.document.getElementById('y1')

    var x2_str = window.document.getElementById('x2')
    var y2_str = window.document.getElementById('y2')

    var x3_str = window.document.getElementById('x3')
    var y3_str = window.document.getElementById('y3')

    var x4_str = window.document.getElementById('x4')
    var y4_str = window.document.getElementById('y4')

    var res = window.document.getElementById('res')
    
    res.innerHTML = '<strong>Deus é bom</strong>'

    if (x1_str.value.length == 0 || y1_str.value.length == 0 || x2_str.value.length == 0 || y2_str.value.length == 0 || x3_str.value.length == 0 || y3_str.value.length == 0 || x4_str.value.length == 0 || y4_str.value.length == 0){
        window.alert('Preencha todos os campos')
        }else{
            // Transformando os "numeros" para números 
            var x1_num = Number(x1_str.value)
            var y1_num = Number(y1_str.value)

            var x2_num = Number(x2_str.value)
            var y2_num = Number(y2_str.value)

            var x3_num = Number(x3_str.value)
            var y3_num = Number(y3_str.value)
            
            var x4_num = Number(x4_str.value)
            var y4_num = Number(y4_str.value)

            // Calcular lados:
            var l1 = Math.sqrt((x2_num - x1_num)**2 + (y2_num - y1_num)**2)
            var l2 = Math.sqrt((x3_num - x2_num)**2 + (y3_num - y2_num)**2)
            var l3 = Math.sqrt((x4_num - x3_num)**2 + (y4_num - y3_num)**2)
            var l4 = Math.sqrt((x1_num - x4_num)**2 + (y1_num - y4_num)**2)

            var lado1 = Math.round(l1*1000)/1000
            var lado2 = Math.round(l2* 1000)/1000
            var lado3 = Math.round(l3*1000)/1000
            var lado4 = Math.round(l4*1000)/1000

            // Verificando os angulos retos atraves de produto escalar
            a1 = (x2_num - x1_num) * (x4_num - x1_num) + (y2_num - y1_num) * (y4_num - y1_num)  
            a2 = (x1_num - x2_num) * (x3_num - x2_num) + (y1_num - y2_num) * (y3_num - y2_num)  
            a3 = (x2_num - x3_num) * (x4_num - x3_num) + (y2_num - y3_num) * (y4_num - y3_num)   
            a4 = (x3_num - x4_num) * (x1_num - x4_num) + (y3_num - y4_num) * (y1_num - y4_num) 
            var anguloreto = (a1 == 0) && (a2 == 0) && (a3 == 0) && (a4 == 0)

            if (anguloreto && lado1 === lado2 && lado2 === lado3 && lado3 === lado4){
                res.innerHTML += 'E quadrado'
                console.log('É quadrado')
            }else if (anguloreto && lado1 === lado3 && lado2 === lado4){
                res.innerHTML += 'É um retangulo'
                console.log('É um retangulo')
            }else{
                res.innerHTML += 'Objeto desconhecido'
                console.log('Objeto desconhecido')
            }
        }


}