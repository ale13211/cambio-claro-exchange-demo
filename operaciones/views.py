from decimal import Decimal, InvalidOperation
from django.http import JsonResponse
from django.shortcuts import render
RATES={"buy":Decimal("7350"),"sell":Decimal("7300")}
def dashboard(request): return render(request,"operaciones/dashboard.html",{"rates":RATES})
def cotizar(request):
 try: amount=Decimal(request.GET.get("monto","0"))
 except InvalidOperation: return JsonResponse({"error":"Monto inválido"},status=400)
 operation=request.GET.get("operacion","buy")
 if operation not in RATES or amount<0: return JsonResponse({"error":"Operación inválida"},status=400)
 return JsonResponse({"guaranies":str(amount*RATES[operation]),"tasa":str(RATES[operation])})