function formatarMoeda(input) {
    // Remove tudo que não for número
    let valor = input.value.replace(/\D/g, '');
  
    // Verificar se o valor tem mais de 2 dígitos para poder adicionar a vírgula
    if (valor.length > 2) {
      // Colocar a vírgula nos dois últimos dígitos
      valor = valor.replace(/(\d+)(\d{2})$/, '$1,$2');
    }
  
    // Adicionar os pontos como separadores de milhar, mas sem ultrapassar os dígitos
    valor = valor.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  
    // Colocar o prefixo "R$" no valor
    if (valor) {
      input.value = 'R$ ' + valor;
    } else {
      input.value = '';
    }
  }
  