<?php
$uploadDir = 'uploads/'; 

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (!empty($_FILES['file']['name'])) {
        
        $randomName = bin2hex(random_bytes(2));
        $fileExtension = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
        $newFileName = $randomName . '.' . $fileExtension;
        $uploadFilePath = $uploadDir . $newFileName;

        
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0777, true);
        }

        
        if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadFilePath)) {
            $fileUrl = 'http://' . $_SERVER['HTTP_HOST'] . '/' . $uploadFilePath;
            echo $fileUrl;
        } else {
            echo "Ошибка загрузки файла."; 
        }
    } else {
        echo "Файл не выбран."; 
    }
}
?>
