import shutil
from pkg_resources import require
from rest_framework import serializers
from .models import Folder,Files


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Files
        fields='__all__'

class FileListSerializer(serializers.Serializer):
    
    files= serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
        max_length=10000,
        allow_empty=False
    )
    folder=serializers.CharField(required = False)

    def zip_files(self,folder):
        return shutil.make_archive(f'public/static/zip/{folder}','zip',f'public/static/{folder}')
    
    def create(self , validated_data):
        folder=Folder.objects.create()
        files=validated_data.pop('files')
        file_objs=[]
        for file in files:
            print(file)
            files_obj=Files.objects.create(folder = folder,file = file)
            file_objs.append(files_obj)

        self.zip_files(folder.uid)    

        return { 'files': {} ,  'folder': str(folder.uid) }