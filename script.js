document.getElementById('form').addEventListener('submit', function(event){
    event.preventDefault();

    const ativo_c = parseFloat(document.getElementById('ativo_c').value);
    const rlp = parseFloat(document.getElementById('rlp').value);
    const passivo_c = parseFloat(document.getElementById('passivo_c').value);
    const passivo_nc = parseFloat(document.getElementById('passivo_nc').value);
    const estoque = parseFloat(document.getElementById('estoque').value);
    const disponivel = parseFloat(document.getElementById('disponivel').value);
    const lucro_l = parseFloat(document.getElementById('lucro_l').value);
    const lucro_b = parseFloat(document.getElementById('lucro_b').value);
    const rol = parseFloat(document.getElementById('rol').value);
    const lair = parseFloat(document.getElementById('lair').value);
    const ativo_t = parseFloat(document.getElementById('ativo_t').value);
    const passivo_t = parseFloat(document.getElementById('passivo_t').value);

    const patrimonio_l = ativo_t - passivo_t;

    const liquidez_g = (ativo_c + rlp) / (passivo_c + passivo_nc);
    const liquidez_c = ativo_c / passivo_c;
    const liquidez_s = (ativo_c - estoque) / passivo_c;
    const liquidez_i = disponivel / passivo_c;
    const mb = lucro_b / rol * 100;
    const mo = lair / rol * 100;
    const ml = lucro_l / rol * 100;
    const roe = patrimonio_l !== 0 ? lucro_l / patrimonio_l * 100 : 0; //evita divisão por 0
    const roa = ativo_t !== 0 ? lucro_l / ativo_t * 100 : 0; //evita divisão por 0
    const comp_end = passivo_c / passivo_t * 100;
    const end_geral = passivo_t / ativo_t * 100;
    const part_cap = patrimonio_l !== 0 ? passivo_t / patrimonio_l * 100 : 0; //evita divisão por 0

    window.location.href = `/valores.html?liquidez_g=${liquidez_g}&liquidez_c=${liquidez_c}&liquidez_s=${liquidez_s}&liquidez_i=${liquidez_i}&mb=${mb}&mo=${mo}&ml=${ml}&roe=${roe}&roa=${roa}&comp_end=${comp_end}&end_geral=${end_geral}&part_cap=${part_cap}`;
});