{"filter":false,"title":"lambda_function.py","tooltip":"/enedbfuncRdsCards/lambda_function.py","undoManager":{"mark":85,"position":85,"stack":[[{"start":{"row":7,"column":0},"end":{"row":8,"column":13},"action":"remove","lines":["import boto3","import base64"],"id":2},{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":18,"column":43},"action":"remove","lines":["","#s3 settings","BUCKET_NAME = os.environ.get('BUCKET_NAME')"],"id":3},{"start":{"row":15,"column":41},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":137,"column":0},"end":{"row":142,"column":83},"action":"remove","lines":["            ","                    s3 = boto3.client('s3')","                    file_path = \"images/\" + result[0].get('userid') + \".png\"","                    responce = s3.get_object(Bucket=BUCKET_NAME, Key=file_path)","                    body = responce['Body'].read()","                    data[k][0]['imageurl'] = base64.b64encode(body).decode('utf-8')"],"id":4},{"start":{"row":136,"column":36},"end":{"row":137,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":191,"column":27},"end":{"row":191,"column":28},"action":"remove","lines":["["],"id":5}],[{"start":{"row":191,"column":27},"end":{"row":191,"column":31},"action":"insert","lines":["get("],"id":6}],[{"start":{"row":191,"column":27},"end":{"row":191,"column":28},"action":"insert","lines":["."],"id":7}],[{"start":{"row":191,"column":38},"end":{"row":191,"column":39},"action":"remove","lines":["]"],"id":8}],[{"start":{"row":191,"column":38},"end":{"row":191,"column":39},"action":"insert","lines":[")"],"id":9}],[{"start":{"row":226,"column":37},"end":{"row":226,"column":38},"action":"remove","lines":["]"],"id":10},{"start":{"row":226,"column":36},"end":{"row":226,"column":37},"action":"remove","lines":["'"]},{"start":{"row":226,"column":35},"end":{"row":226,"column":36},"action":"remove","lines":["a"]},{"start":{"row":226,"column":34},"end":{"row":226,"column":35},"action":"remove","lines":["t"]},{"start":{"row":226,"column":33},"end":{"row":226,"column":34},"action":"remove","lines":["a"]},{"start":{"row":226,"column":32},"end":{"row":226,"column":33},"action":"remove","lines":["d"]},{"start":{"row":226,"column":31},"end":{"row":226,"column":32},"action":"remove","lines":["'"]},{"start":{"row":226,"column":30},"end":{"row":226,"column":31},"action":"remove","lines":["["]}],[{"start":{"row":226,"column":30},"end":{"row":226,"column":42},"action":"insert","lines":[".get('data')"],"id":11}],[{"start":{"row":227,"column":37},"end":{"row":227,"column":38},"action":"remove","lines":["]"],"id":12},{"start":{"row":227,"column":36},"end":{"row":227,"column":37},"action":"remove","lines":["'"]},{"start":{"row":227,"column":35},"end":{"row":227,"column":36},"action":"remove","lines":["a"]},{"start":{"row":227,"column":34},"end":{"row":227,"column":35},"action":"remove","lines":["t"]},{"start":{"row":227,"column":33},"end":{"row":227,"column":34},"action":"remove","lines":["a"]},{"start":{"row":227,"column":32},"end":{"row":227,"column":33},"action":"remove","lines":["d"]},{"start":{"row":227,"column":31},"end":{"row":227,"column":32},"action":"remove","lines":["'"]},{"start":{"row":227,"column":30},"end":{"row":227,"column":31},"action":"remove","lines":["["]}],[{"start":{"row":227,"column":30},"end":{"row":227,"column":42},"action":"insert","lines":[".get('data')"],"id":13}],[{"start":{"row":228,"column":37},"end":{"row":228,"column":38},"action":"remove","lines":["]"],"id":14},{"start":{"row":228,"column":36},"end":{"row":228,"column":37},"action":"remove","lines":["'"]},{"start":{"row":228,"column":35},"end":{"row":228,"column":36},"action":"remove","lines":["a"]},{"start":{"row":228,"column":34},"end":{"row":228,"column":35},"action":"remove","lines":["t"]},{"start":{"row":228,"column":33},"end":{"row":228,"column":34},"action":"remove","lines":["a"]},{"start":{"row":228,"column":32},"end":{"row":228,"column":33},"action":"remove","lines":["d"]},{"start":{"row":228,"column":31},"end":{"row":228,"column":32},"action":"remove","lines":["'"]},{"start":{"row":228,"column":30},"end":{"row":228,"column":31},"action":"remove","lines":["["]}],[{"start":{"row":228,"column":30},"end":{"row":228,"column":42},"action":"insert","lines":[".get('data')"],"id":15}],[{"start":{"row":229,"column":37},"end":{"row":229,"column":38},"action":"remove","lines":["]"],"id":16},{"start":{"row":229,"column":36},"end":{"row":229,"column":37},"action":"remove","lines":["'"]},{"start":{"row":229,"column":35},"end":{"row":229,"column":36},"action":"remove","lines":["a"]},{"start":{"row":229,"column":34},"end":{"row":229,"column":35},"action":"remove","lines":["t"]},{"start":{"row":229,"column":33},"end":{"row":229,"column":34},"action":"remove","lines":["a"]},{"start":{"row":229,"column":32},"end":{"row":229,"column":33},"action":"remove","lines":["d"]},{"start":{"row":229,"column":31},"end":{"row":229,"column":32},"action":"remove","lines":["'"]},{"start":{"row":229,"column":30},"end":{"row":229,"column":31},"action":"remove","lines":["["]}],[{"start":{"row":229,"column":30},"end":{"row":229,"column":31},"action":"insert","lines":["v"],"id":17}],[{"start":{"row":229,"column":30},"end":{"row":229,"column":31},"action":"remove","lines":["v"],"id":18}],[{"start":{"row":229,"column":30},"end":{"row":229,"column":42},"action":"insert","lines":[".get('data')"],"id":19}],[{"start":{"row":191,"column":31},"end":{"row":191,"column":32},"action":"remove","lines":["("],"id":20},{"start":{"row":191,"column":30},"end":{"row":191,"column":31},"action":"remove","lines":["t"]},{"start":{"row":191,"column":29},"end":{"row":191,"column":30},"action":"remove","lines":["e"]},{"start":{"row":191,"column":28},"end":{"row":191,"column":29},"action":"remove","lines":["g"]},{"start":{"row":191,"column":27},"end":{"row":191,"column":28},"action":"remove","lines":["."]}],[{"start":{"row":191,"column":27},"end":{"row":191,"column":28},"action":"insert","lines":["["],"id":21}],[{"start":{"row":191,"column":34},"end":{"row":191,"column":35},"action":"remove","lines":[")"],"id":22}],[{"start":{"row":191,"column":34},"end":{"row":191,"column":35},"action":"insert","lines":["]"],"id":23}],[{"start":{"row":188,"column":79},"end":{"row":189,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":189,"column":0},"end":{"row":189,"column":4},"action":"insert","lines":["    "]},{"start":{"row":189,"column":4},"end":{"row":189,"column":5},"action":"insert","lines":["p"]},{"start":{"row":189,"column":5},"end":{"row":189,"column":6},"action":"insert","lines":["r"]},{"start":{"row":189,"column":6},"end":{"row":189,"column":7},"action":"insert","lines":["i"]},{"start":{"row":189,"column":7},"end":{"row":189,"column":8},"action":"insert","lines":["n"]},{"start":{"row":189,"column":8},"end":{"row":189,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":189,"column":9},"end":{"row":189,"column":11},"action":"insert","lines":["()"],"id":25}],[{"start":{"row":189,"column":10},"end":{"row":189,"column":11},"action":"insert","lines":["c"],"id":26},{"start":{"row":189,"column":11},"end":{"row":189,"column":12},"action":"insert","lines":["a"]},{"start":{"row":189,"column":12},"end":{"row":189,"column":13},"action":"insert","lines":["r"]},{"start":{"row":189,"column":13},"end":{"row":189,"column":14},"action":"insert","lines":["d"]},{"start":{"row":189,"column":14},"end":{"row":189,"column":15},"action":"insert","lines":["i"]},{"start":{"row":189,"column":15},"end":{"row":189,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":227,"column":41},"end":{"row":227,"column":42},"action":"remove","lines":[")"],"id":27}],[{"start":{"row":227,"column":41},"end":{"row":227,"column":42},"action":"insert","lines":["]"],"id":28}],[{"start":{"row":227,"column":34},"end":{"row":227,"column":35},"action":"remove","lines":["("],"id":29},{"start":{"row":227,"column":33},"end":{"row":227,"column":34},"action":"remove","lines":["t"]},{"start":{"row":227,"column":32},"end":{"row":227,"column":33},"action":"remove","lines":["e"]},{"start":{"row":227,"column":31},"end":{"row":227,"column":32},"action":"remove","lines":["g"]},{"start":{"row":227,"column":30},"end":{"row":227,"column":31},"action":"remove","lines":["."]}],[{"start":{"row":227,"column":30},"end":{"row":227,"column":31},"action":"insert","lines":["["],"id":30}],[{"start":{"row":228,"column":41},"end":{"row":228,"column":42},"action":"remove","lines":[")"],"id":31},{"start":{"row":228,"column":40},"end":{"row":228,"column":41},"action":"remove","lines":["'"]},{"start":{"row":228,"column":39},"end":{"row":228,"column":40},"action":"remove","lines":["a"]},{"start":{"row":228,"column":38},"end":{"row":228,"column":39},"action":"remove","lines":["t"]},{"start":{"row":228,"column":37},"end":{"row":228,"column":38},"action":"remove","lines":["a"]},{"start":{"row":228,"column":36},"end":{"row":228,"column":37},"action":"remove","lines":["d"]},{"start":{"row":228,"column":35},"end":{"row":228,"column":36},"action":"remove","lines":["'"]},{"start":{"row":228,"column":34},"end":{"row":228,"column":35},"action":"remove","lines":["("]},{"start":{"row":228,"column":33},"end":{"row":228,"column":34},"action":"remove","lines":["t"]},{"start":{"row":228,"column":32},"end":{"row":228,"column":33},"action":"remove","lines":["e"]},{"start":{"row":228,"column":31},"end":{"row":228,"column":32},"action":"remove","lines":["g"]},{"start":{"row":228,"column":30},"end":{"row":228,"column":31},"action":"remove","lines":["."]}],[{"start":{"row":228,"column":30},"end":{"row":228,"column":38},"action":"insert","lines":["['data']"],"id":32}],[{"start":{"row":229,"column":41},"end":{"row":229,"column":42},"action":"remove","lines":[")"],"id":33},{"start":{"row":229,"column":40},"end":{"row":229,"column":41},"action":"remove","lines":["'"]},{"start":{"row":229,"column":39},"end":{"row":229,"column":40},"action":"remove","lines":["a"]},{"start":{"row":229,"column":38},"end":{"row":229,"column":39},"action":"remove","lines":["t"]},{"start":{"row":229,"column":37},"end":{"row":229,"column":38},"action":"remove","lines":["a"]},{"start":{"row":229,"column":36},"end":{"row":229,"column":37},"action":"remove","lines":["d"]},{"start":{"row":229,"column":35},"end":{"row":229,"column":36},"action":"remove","lines":["'"]},{"start":{"row":229,"column":34},"end":{"row":229,"column":35},"action":"remove","lines":["("]},{"start":{"row":229,"column":33},"end":{"row":229,"column":34},"action":"remove","lines":["t"]},{"start":{"row":229,"column":32},"end":{"row":229,"column":33},"action":"remove","lines":["e"]},{"start":{"row":229,"column":31},"end":{"row":229,"column":32},"action":"remove","lines":["g"]},{"start":{"row":229,"column":30},"end":{"row":229,"column":31},"action":"remove","lines":["."]}],[{"start":{"row":229,"column":30},"end":{"row":229,"column":38},"action":"insert","lines":["['data']"],"id":34}],[{"start":{"row":230,"column":41},"end":{"row":230,"column":42},"action":"remove","lines":[")"],"id":35},{"start":{"row":230,"column":40},"end":{"row":230,"column":41},"action":"remove","lines":["'"]},{"start":{"row":230,"column":39},"end":{"row":230,"column":40},"action":"remove","lines":["a"]},{"start":{"row":230,"column":38},"end":{"row":230,"column":39},"action":"remove","lines":["t"]},{"start":{"row":230,"column":37},"end":{"row":230,"column":38},"action":"remove","lines":["a"]},{"start":{"row":230,"column":36},"end":{"row":230,"column":37},"action":"remove","lines":["d"]},{"start":{"row":230,"column":35},"end":{"row":230,"column":36},"action":"remove","lines":["'"]},{"start":{"row":230,"column":34},"end":{"row":230,"column":35},"action":"remove","lines":["("]},{"start":{"row":230,"column":33},"end":{"row":230,"column":34},"action":"remove","lines":["t"]},{"start":{"row":230,"column":32},"end":{"row":230,"column":33},"action":"remove","lines":["e"]},{"start":{"row":230,"column":31},"end":{"row":230,"column":32},"action":"remove","lines":["g"]}],[{"start":{"row":230,"column":30},"end":{"row":230,"column":31},"action":"remove","lines":["."],"id":36}],[{"start":{"row":230,"column":30},"end":{"row":230,"column":38},"action":"insert","lines":["['data']"],"id":37}],[{"start":{"row":190,"column":53},"end":{"row":190,"column":54},"action":"insert","lines":["c"],"id":38},{"start":{"row":190,"column":54},"end":{"row":190,"column":55},"action":"insert","lines":["a"]},{"start":{"row":190,"column":55},"end":{"row":190,"column":56},"action":"insert","lines":["r"]},{"start":{"row":190,"column":56},"end":{"row":190,"column":57},"action":"insert","lines":["d"]}],[{"start":{"row":189,"column":16},"end":{"row":189,"column":17},"action":"remove","lines":[")"],"id":39},{"start":{"row":189,"column":15},"end":{"row":189,"column":16},"action":"remove","lines":["d"]},{"start":{"row":189,"column":14},"end":{"row":189,"column":15},"action":"remove","lines":["i"]},{"start":{"row":189,"column":13},"end":{"row":189,"column":14},"action":"remove","lines":["d"]},{"start":{"row":189,"column":12},"end":{"row":189,"column":13},"action":"remove","lines":["r"]},{"start":{"row":189,"column":11},"end":{"row":189,"column":12},"action":"remove","lines":["a"]},{"start":{"row":189,"column":10},"end":{"row":189,"column":11},"action":"remove","lines":["c"]},{"start":{"row":189,"column":9},"end":{"row":189,"column":10},"action":"remove","lines":["("]},{"start":{"row":189,"column":8},"end":{"row":189,"column":9},"action":"remove","lines":["t"]},{"start":{"row":189,"column":7},"end":{"row":189,"column":8},"action":"remove","lines":["n"]},{"start":{"row":189,"column":6},"end":{"row":189,"column":7},"action":"remove","lines":["i"]},{"start":{"row":189,"column":5},"end":{"row":189,"column":6},"action":"remove","lines":["r"]},{"start":{"row":189,"column":4},"end":{"row":189,"column":5},"action":"remove","lines":["p"]},{"start":{"row":189,"column":0},"end":{"row":189,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":188,"column":79},"end":{"row":189,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":191,"column":33},"end":{"row":191,"column":34},"action":"remove","lines":["'"],"id":41},{"start":{"row":191,"column":32},"end":{"row":191,"column":33},"action":"remove","lines":["a"]},{"start":{"row":191,"column":31},"end":{"row":191,"column":32},"action":"remove","lines":["t"]},{"start":{"row":191,"column":30},"end":{"row":191,"column":31},"action":"remove","lines":["a"]},{"start":{"row":191,"column":29},"end":{"row":191,"column":30},"action":"remove","lines":["d"]},{"start":{"row":191,"column":28},"end":{"row":191,"column":29},"action":"remove","lines":["'"]}],[{"start":{"row":191,"column":28},"end":{"row":191,"column":29},"action":"insert","lines":["0"],"id":42}],[{"start":{"row":191,"column":36},"end":{"row":191,"column":37},"action":"insert","lines":["u"],"id":43},{"start":{"row":191,"column":37},"end":{"row":191,"column":38},"action":"insert","lines":["s"]},{"start":{"row":191,"column":38},"end":{"row":191,"column":39},"action":"insert","lines":["e"]},{"start":{"row":191,"column":39},"end":{"row":191,"column":40},"action":"insert","lines":["r"]}],[{"start":{"row":181,"column":21},"end":{"row":182,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"insert","lines":["    "]},{"start":{"row":182,"column":4},"end":{"row":183,"column":0},"action":"insert","lines":["",""]},{"start":{"row":183,"column":0},"end":{"row":183,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":183,"column":4},"end":{"row":183,"column":14},"action":"insert","lines":["json.loads"],"id":45}],[{"start":{"row":183,"column":13},"end":{"row":183,"column":14},"action":"remove","lines":["s"],"id":46},{"start":{"row":183,"column":12},"end":{"row":183,"column":13},"action":"remove","lines":["d"]},{"start":{"row":183,"column":11},"end":{"row":183,"column":12},"action":"remove","lines":["a"]},{"start":{"row":183,"column":10},"end":{"row":183,"column":11},"action":"remove","lines":["o"]},{"start":{"row":183,"column":9},"end":{"row":183,"column":10},"action":"remove","lines":["l"]},{"start":{"row":183,"column":8},"end":{"row":183,"column":9},"action":"remove","lines":["."]},{"start":{"row":183,"column":7},"end":{"row":183,"column":8},"action":"remove","lines":["n"]},{"start":{"row":183,"column":6},"end":{"row":183,"column":7},"action":"remove","lines":["o"]},{"start":{"row":183,"column":5},"end":{"row":183,"column":6},"action":"remove","lines":["s"]},{"start":{"row":183,"column":4},"end":{"row":183,"column":5},"action":"remove","lines":["j"]}],[{"start":{"row":183,"column":4},"end":{"row":183,"column":40},"action":"insert","lines":["payload = json.loads(event['body']);"],"id":47}],[{"start":{"row":183,"column":29},"end":{"row":183,"column":30},"action":"remove","lines":["t"],"id":48},{"start":{"row":183,"column":28},"end":{"row":183,"column":29},"action":"remove","lines":["n"]},{"start":{"row":183,"column":27},"end":{"row":183,"column":28},"action":"remove","lines":["e"]},{"start":{"row":183,"column":26},"end":{"row":183,"column":27},"action":"remove","lines":["v"]},{"start":{"row":183,"column":25},"end":{"row":183,"column":26},"action":"remove","lines":["e"]}],[{"start":{"row":183,"column":25},"end":{"row":183,"column":26},"action":"insert","lines":["x"],"id":49}],[{"start":{"row":183,"column":4},"end":{"row":183,"column":36},"action":"remove","lines":["payload = json.loads(x['body']);"],"id":50}],[{"start":{"row":183,"column":0},"end":{"row":183,"column":4},"action":"remove","lines":["    "],"id":51},{"start":{"row":182,"column":4},"end":{"row":183,"column":0},"action":"remove","lines":["",""]},{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"remove","lines":["    "]},{"start":{"row":181,"column":21},"end":{"row":182,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":185,"column":37},"end":{"row":186,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":186,"column":0},"end":{"row":186,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":186,"column":4},"end":{"row":186,"column":8},"action":"remove","lines":["    "],"id":53}],[{"start":{"row":186,"column":4},"end":{"row":187,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":187,"column":4},"end":{"row":187,"column":36},"action":"insert","lines":["payload = json.loads(x['body']);"],"id":55}],[{"start":{"row":193,"column":26},"end":{"row":193,"column":27},"action":"remove","lines":["]"],"id":57},{"start":{"row":193,"column":25},"end":{"row":193,"column":26},"action":"remove","lines":["'"]},{"start":{"row":193,"column":24},"end":{"row":193,"column":25},"action":"remove","lines":["y"]},{"start":{"row":193,"column":23},"end":{"row":193,"column":24},"action":"remove","lines":["d"]},{"start":{"row":193,"column":22},"end":{"row":193,"column":23},"action":"remove","lines":["o"]},{"start":{"row":193,"column":21},"end":{"row":193,"column":22},"action":"remove","lines":["b"]},{"start":{"row":193,"column":20},"end":{"row":193,"column":21},"action":"remove","lines":["'"]},{"start":{"row":193,"column":19},"end":{"row":193,"column":20},"action":"remove","lines":["["]},{"start":{"row":193,"column":18},"end":{"row":193,"column":19},"action":"remove","lines":["x"]}],[{"start":{"row":193,"column":18},"end":{"row":193,"column":25},"action":"insert","lines":["payload"],"id":58}],[{"start":{"row":193,"column":26},"end":{"row":193,"column":27},"action":"remove","lines":["0"],"id":59}],[{"start":{"row":193,"column":26},"end":{"row":193,"column":28},"action":"insert","lines":["''"],"id":60}],[{"start":{"row":193,"column":27},"end":{"row":193,"column":28},"action":"insert","lines":["d"],"id":61},{"start":{"row":193,"column":28},"end":{"row":193,"column":29},"action":"insert","lines":["a"]},{"start":{"row":193,"column":29},"end":{"row":193,"column":30},"action":"insert","lines":["t"]},{"start":{"row":193,"column":30},"end":{"row":193,"column":31},"action":"insert","lines":["a"]}],[{"start":{"row":203,"column":32},"end":{"row":203,"column":33},"action":"remove","lines":["x"],"id":62}],[{"start":{"row":203,"column":32},"end":{"row":203,"column":39},"action":"insert","lines":["payload"],"id":63}],[{"start":{"row":228,"column":29},"end":{"row":228,"column":30},"action":"remove","lines":["]"],"id":64},{"start":{"row":228,"column":28},"end":{"row":228,"column":29},"action":"remove","lines":["'"]},{"start":{"row":228,"column":27},"end":{"row":228,"column":28},"action":"remove","lines":["y"]},{"start":{"row":228,"column":26},"end":{"row":228,"column":27},"action":"remove","lines":["d"]},{"start":{"row":228,"column":25},"end":{"row":228,"column":26},"action":"remove","lines":["o"]},{"start":{"row":228,"column":24},"end":{"row":228,"column":25},"action":"remove","lines":["b"]},{"start":{"row":228,"column":23},"end":{"row":228,"column":24},"action":"remove","lines":["'"]},{"start":{"row":228,"column":22},"end":{"row":228,"column":23},"action":"remove","lines":["["]}],[{"start":{"row":229,"column":29},"end":{"row":229,"column":30},"action":"remove","lines":["]"],"id":65},{"start":{"row":229,"column":28},"end":{"row":229,"column":29},"action":"remove","lines":["'"]},{"start":{"row":229,"column":27},"end":{"row":229,"column":28},"action":"remove","lines":["y"]},{"start":{"row":229,"column":26},"end":{"row":229,"column":27},"action":"remove","lines":["d"]},{"start":{"row":229,"column":25},"end":{"row":229,"column":26},"action":"remove","lines":["o"]},{"start":{"row":229,"column":24},"end":{"row":229,"column":25},"action":"remove","lines":["b"]},{"start":{"row":229,"column":23},"end":{"row":229,"column":24},"action":"remove","lines":["'"]},{"start":{"row":229,"column":22},"end":{"row":229,"column":23},"action":"remove","lines":["["]}],[{"start":{"row":230,"column":29},"end":{"row":230,"column":30},"action":"remove","lines":["]"],"id":66},{"start":{"row":230,"column":28},"end":{"row":230,"column":29},"action":"remove","lines":["'"]},{"start":{"row":230,"column":27},"end":{"row":230,"column":28},"action":"remove","lines":["y"]},{"start":{"row":230,"column":26},"end":{"row":230,"column":27},"action":"remove","lines":["d"]},{"start":{"row":230,"column":25},"end":{"row":230,"column":26},"action":"remove","lines":["o"]},{"start":{"row":230,"column":24},"end":{"row":230,"column":25},"action":"remove","lines":["b"]},{"start":{"row":230,"column":23},"end":{"row":230,"column":24},"action":"remove","lines":["'"]},{"start":{"row":230,"column":22},"end":{"row":230,"column":23},"action":"remove","lines":["["]}],[{"start":{"row":231,"column":29},"end":{"row":231,"column":30},"action":"remove","lines":["]"],"id":67},{"start":{"row":231,"column":28},"end":{"row":231,"column":29},"action":"remove","lines":["'"]},{"start":{"row":231,"column":27},"end":{"row":231,"column":28},"action":"remove","lines":["y"]},{"start":{"row":231,"column":26},"end":{"row":231,"column":27},"action":"remove","lines":["d"]},{"start":{"row":231,"column":25},"end":{"row":231,"column":26},"action":"remove","lines":["o"]},{"start":{"row":231,"column":24},"end":{"row":231,"column":25},"action":"remove","lines":["b"]},{"start":{"row":231,"column":23},"end":{"row":231,"column":24},"action":"remove","lines":["'"]}],[{"start":{"row":231,"column":22},"end":{"row":231,"column":23},"action":"remove","lines":["["],"id":68}],[{"start":{"row":229,"column":44},"end":{"row":229,"column":45},"action":"insert","lines":["I"],"id":69},{"start":{"row":229,"column":45},"end":{"row":229,"column":46},"action":"insert","lines":["d"]}],[{"start":{"row":230,"column":42},"end":{"row":230,"column":43},"action":"insert","lines":["I"],"id":70},{"start":{"row":230,"column":43},"end":{"row":230,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":231,"column":0},"end":{"row":231,"column":1},"action":"insert","lines":["#"],"id":71}],[{"start":{"row":240,"column":0},"end":{"row":240,"column":1},"action":"insert","lines":["#"],"id":72}],[{"start":{"row":241,"column":0},"end":{"row":241,"column":1},"action":"insert","lines":["#"],"id":73}],[{"start":{"row":272,"column":17},"end":{"row":272,"column":28},"action":"remove","lines":["likeUserIds"],"id":74},{"start":{"row":272,"column":17},"end":{"row":272,"column":31},"action":"insert","lines":["empathyUserIds"]}],[{"start":{"row":272,"column":36},"end":{"row":272,"column":37},"action":"remove","lines":["}"],"id":75},{"start":{"row":272,"column":35},"end":{"row":272,"column":36},"action":"remove","lines":["{"]}],[{"start":{"row":272,"column":35},"end":{"row":272,"column":36},"action":"insert","lines":["["],"id":76},{"start":{"row":272,"column":36},"end":{"row":272,"column":37},"action":"insert","lines":["]"]}],[{"start":{"row":193,"column":39},"end":{"row":193,"column":45},"action":"remove","lines":["userid"],"id":78},{"start":{"row":193,"column":39},"end":{"row":193,"column":51},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":193,"column":8},"end":{"row":193,"column":14},"action":"remove","lines":["userid"],"id":79},{"start":{"row":193,"column":8},"end":{"row":193,"column":20},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":196,"column":21},"end":{"row":196,"column":27},"action":"remove","lines":["userid"],"id":80},{"start":{"row":196,"column":21},"end":{"row":196,"column":33},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":199,"column":41},"end":{"row":199,"column":47},"action":"remove","lines":["userid"],"id":81},{"start":{"row":199,"column":41},"end":{"row":199,"column":53},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":205,"column":30},"end":{"row":205,"column":36},"action":"remove","lines":["userid"],"id":82},{"start":{"row":205,"column":30},"end":{"row":205,"column":42},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":208,"column":34},"end":{"row":208,"column":40},"action":"remove","lines":["userid"],"id":83},{"start":{"row":208,"column":34},"end":{"row":208,"column":46},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":213,"column":42},"end":{"row":213,"column":48},"action":"remove","lines":["userid"],"id":84},{"start":{"row":213,"column":42},"end":{"row":213,"column":54},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":217,"column":42},"end":{"row":217,"column":48},"action":"remove","lines":["userid"],"id":85},{"start":{"row":217,"column":42},"end":{"row":217,"column":54},"action":"insert","lines":["empathizerid"]}],[{"start":{"row":229,"column":44},"end":{"row":229,"column":45},"action":"remove","lines":["I"],"id":86}],[{"start":{"row":229,"column":44},"end":{"row":229,"column":45},"action":"insert","lines":["i"],"id":87}],[{"start":{"row":230,"column":42},"end":{"row":230,"column":43},"action":"remove","lines":["I"],"id":88}],[{"start":{"row":230,"column":42},"end":{"row":230,"column":43},"action":"insert","lines":["i"],"id":89}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":232,"column":4},"end":{"row":232,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1620609585936,"hash":"5399833c3e453d18971c18c320cb504e1a9586cd"}