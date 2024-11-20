<?php
require('fpdf/fpdf.php');

if ($_SERVER["REQUEST_METHOD"] == "POST"){

    $liquidez_g = $_POST["liquidez_g"];
    $liquidez_c = $_POST["liquidez_c"];
    $liquidez_s = $_POST["liquidez_s"];
    $liquidez_i = $_POST["liquidez_i"];

    $mb = $_POST["mb"];
    $mo = $_POST["mo"];
    $ml = $_POST["ml"];
    $roe = $_POST["roe"];
    $roa = $_POST["roa"];

    $comp_end = $_POST["comp_end"];
    $end_geral = $_POST["end_geral"];
    $part_cap = $_POST["part_cap"];
    
    $pdf = new FPDF();
    $pdf -> AddPage();

    $pdf->SetFont('Arial', 'B', 20);
    $pdf->SetFillColor(230, 230, 230);
    $pdf->Cell(190, 10, 'Balanceamento da sua empresa', 0, 1, 'C');
    $pdf->Ln();

    $pdf->SetFont('Arial', 'B', 18);
    $pdf->Cell(190, 15, 'Liquidez', 1, 1, 'C', true);

    $pdf->SetFont('Arial', '', 16);
    $pdf->Cell(95, 10, 'Liquidez Geral ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $liquidez_g, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Liquidez Corrente ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $liquidez_c, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Liquidez Seca ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $liquidez_s, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Liquidez Imediata ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $liquidez_i, 1, 1, 'C');
    $pdf->Ln();

    $pdf->SetFont('Arial', 'B', 18);
    $pdf->Cell(190, 15, 'Rentabilidade', 1, 1, 'C', true);

    $pdf->SetFont('Arial', '', 16);
    $pdf->Cell(95, 10, 'Margem Bruta ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $mb, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Margem Operacional ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $mo, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Margem Líquida ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $ml, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Retorno sobre o PL (ROE) ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $roe, 1, 1, 'C');
    $pdf->Cell(190, 10, 'Retorno sobre os Ativos (RSI ou ROA) ', 1, 1, 'C', true);
    $pdf->Cell(190, 10, $roa, 1, 1, 'C');
    $pdf->Ln();

    $pdf->SetFont('Arial', 'B', 18);
    $pdf->Cell(190, 15, 'Endividamento', 1, 1, 'C', true);

    $pdf->SetFont('Arial', '', 16);
    $pdf->Cell(95, 10, 'Composição do Endividamento ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $comp_end, 1, 1, 'C');
    $pdf->Cell(95, 10, 'Endividamento Geral ', 1, 0, 'C', true);
    $pdf->Cell(95, 10, $end_geral, 1, 1, 'C');
    $pdf->Cell(190, 10, 'Participação do Capital de Terceiros ', 1, 1, 'C', true);
    $pdf->Cell(190, 10, $part_cap, 1, 1, 'C');
    $pdf->Ln();

    date_default_timezone_set('America/Belem');
    $currentDate = date("d/m/Y");
    $currentHour = date("H:m:s");

    $pdf->SetFont('Arial', '', 12);
    $pdf->Cell(0, 10, 'Data: ' . $currentDate, 0, 1, 'C');
    $pdf->Cell(0, 10, 'Horário: ' . $currentHour, 0, 1, 'C');

    $pdf->Output('balanceamento.pdf', 'D');

}

?>