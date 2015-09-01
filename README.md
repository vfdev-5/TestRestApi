
# Test REST Api

Example of REST Api with users
- Django
- Django REST Framework
- ...

## API description :

The api stores images that authenticated users can upload to the api.
Any user can request all images
    (GET) <URL>/api/photo/
or a particular image by its id, e.g:
    (GET) <URL>/api/photo/1/

An authenticated user can upload an image. For example, using CURL:







