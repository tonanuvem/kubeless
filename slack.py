import json
import requests

url = "https://INSERIR-WEBHOOK"
canal = "#fiap"

def handler(event, context):
    try:
        print(event)
        if not 'msg' in event['data']:
            return 'Campo vazio : msg'
        texto=event['data']['msg']
        print("Texto = "+ texto)
        return postMSG_criada_para_o_slack(texto)
        
    except Exception as e:
        erro = "Erro na function: " + repr(e);
        print(erro)
        return erro
    
def postMSG_criada_para_o_slack(msg):
    # format payload for slack
    sdata = formatForSlack(msg)
    r = requests.post(url, sdata, headers={'Content-Type': 'application/json'})
    if r.status_code == 200:
      return 'SUCCEDED: Sent slack webhook.  Msg = ' + msg
    else:
      return 'FAILED: Send slack webhook'

def formatForSlack(msg):
  payload = {
    "channel":canal,
    "username":'ALUNO_Serverless',
    "text": msg,
    "icon_emoji":':cyclone'
  }
  return json.dumps(payload)
