from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
def main(request):
	if request.method=='GET':	
                return render_to_response('graph.html',{})
	else:	
		data_string=request.POST.get('data')	
		adjacentlist=json.loads(data_string)
		colors=[0,1,2,3,4,5,6,7,8,9]
		color_list=[-1]*len(adjacentlist)
		for vertex in range(len(adjacentlist)):
			adj_vertices=adjacentlist[vertex]
			adj_colors=[]	
			for  adj in adj_vertices:
				adj_colors.append(color_list[adj])
			color_list[vertex]=list(set(colors)-set(adj_colors))[0]			
		color_string = json.dumps(color_list)
		return HttpResponse(color_string)
		
