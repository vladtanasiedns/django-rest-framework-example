from rest_framework.views import APIView
from rest_framework.response import Response
from django_rest_tutorial.serializers import TaskSerializer
from django_rest_tutorial.models.Task import Task

class TaskView(APIView):
    """
    Class view where each function represents an http request method
    """
    def get(self, request, format=None):
        queryset = Task.objects.all() # Finds all object using the Task model
        serializer = TaskSerializer(queryset, many=True) # Deserializes the object to JSON format
        return Response(serializer.data) # Returns the result as JSON Format
    
    def post(self, request, format=None):
        task = Task() # Creates the task object
        serializer = TaskSerializer(task, data=request.data) # Serializes the Task object with the passed data in the request

        if serializer.is_valid():
            serializer.save() # Saves the serialized Task object
            return Response(serializer.data, status=200) # Returns the new object and a status of success
        return Response(serializer.errors, 400) # Returns errors and the status of 400

    def patch(self, request, format=None):
        try:
            task = Task.objects.get(id=request.query_params['id']) # Finds the task object with the passed id in the query patam `?id=1`
        except:
            return Response(status=404) # Returns error of the Task is not found
        
        serializer = TaskSerializer(task, data=request.data) # Serializes the Task object with the new data
        if serializer.is_valid():
            serializer.save() # Saves the serialized object
            return Response(serializer.data, status=200)
        return Response(serializer.errors, 400)

    def delete(self, request, format=None):
        try:
            task = Task.objects.get(id=request.query_params['id']) # finds the Task object in the database
        except:
            return Response(status=404)
        
        operation = task.delete() # Deletes the task object with the specified id in `?id=1`
        return Response({ "operation": operation }, status=200)