# Продвинутый ООП, исключения

## Описание/Пошаговая инструкция выполнения домашнего задания:

* в проекте мы работаем с медиа-файлами (аудио, видео, фото)
* есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики (имя, размер, дата создания, владелец...)
* для каждого типа медиа-фалов есть свой набор мета-данных
* попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд)
* приведите примеры кода - как можно создать, обновить, удалить или провести какое-нибудь действие (конвертация, извлечение фич) над файлом (можно без реализации деталей)
* попробуйте дописать классы для работы с файлами, расположенными не на локальном диске (облако, удаленный сервер, s3-like storage)
* попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?

! суть задания - именно проектирование классовой иерархии, а не реализация самой логики, поэтому достаточно, например, просто объявить метод .save(...) и в комментарии уточнить - что он должен делать, без конкретной релаизации


## Media Files

### Common Mediafile Metadata

* filename (/media/files/outs.mp4)
* name ("Lesson #1")
* filesize (123456 bytes)
* created (988689600)
* owner (username)

### Audio Metadata

* format (MP4A)
* rate (48000 Hz)
* channels (stereo)

### Video Metadata

* resolution (720x404)
    * width
    * height
* format (H264)
* bitrate (677 kbps)

### Image Metadata

* size (740x435)
    * width (740)
    * height (435)
* resolution (72x72 ppi)
* colorspace (RGB)

## Operations

### Create

1. From a buffer
    * Pass a buffer with data to make function
    * Detect type from the buffer
2. From a file
    * Pass a file path to make function
    * Detect type from the file content

### Convert

1. Create MediaFile object from file
2. Save MediaFile

### Get metadata info

* List all props
* Get a prop defined by name
