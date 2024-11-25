<?php
// Чтение XML-файла
$xml_file = 'stock.xml';
if (file_exists($xml_file)) {
    $products = simplexml_load_file($xml_file);
} else {
    die('Ошибка: файл XML не найден.');
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Остатки товара</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Остатки товара</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Название</th>
                <th>Остаток</th>
                <th>Цена</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($products->product as $product): ?>
                <tr>
                    <td><?= htmlspecialchars($product->id) ?></td>
                    <td><?= htmlspecialchars($product->name) ?></td>
                    <td><?= htmlspecialchars($product->stock) ?></td>
                    <td><?= htmlspecialchars($product->price) ?> руб.</td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
