class Demo:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":{
                "clip":("CLIP",),
                "pos_text": ("STRING", {
                    "multiline": True,
                    "default": "positive text"
                }),
                "neg_text": ("STRING", {
                    "multiline": True,
                    "default": "negative text"
                }),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING")  #返回类型，为两个输出口

    FUNCTION = "test"  #函数

    CATEGORY = "Hua"   #类传递名称在UI显示

    def test(self, clip, pos_text, neg_text): #定义了一个名为 test 的方法，该方法接受参数：self，clip，pos_text 和 neg_text
        tokens_pos = clip.tokenize(pos_text)   #使用 clip.tokenize() 方法将 pos_text分词为标记(tokens)。然后使用 clip.encode_from_tokens() 方法对这些标记进行编码
        cond_pos, pooled = clip.encode_from_tokens(tokens_pos, return_pooled=True) #调用 encode_from_tokens 方法，传递了一个名为 tokens_neg 的标记列表作为参数

        tokens_neg = clip.tokenize(neg_text)  #使用 clip.tokenize() 方法将 neg_text分词为标记(tokens)。然后使用 clip.encode_from_tokens() 方法对这些标记进行编码 
        cond_neg, pooled = clip.encode_from_tokens(tokens_neg, return_pooled=True) # 调用 encode_from_tokens 方法，传递了一个名为 tokens_neg 的标记列表作为参数
        #方法返回两个值：cond_neg 和 pooled。cond_neg 可能是对负面文本的编码，而 pooled 可能是对整个文本的汇总编码。
        #使用名为 clip 的对象，可能是一个用于文本编码的模型，OpenAI 的 CLIP 模型。设置参数 return_pooled=True，以便方法返回汇总的编码结果。
        #总结这行代码的作用是使用 CLIP 模型对负面文本进行编码，并返回编码后的结果以及相应的汇总编码。


        return (  #返回 （输出）
            [[cond_pos, {"pooled_output": pooled}]], #包含了 pos_text 的编码结果和相应的汇总编码，
            [[cond_neg, {"pooled_output": pooled}]], #包含了 neg_text 的编码结果和相应的汇总编码，
        
        )



NODE_CLASS_MAPPINGS = {   #这段代码定义字典变量，将节点名称映射到相应的类，将字符串Hua映射到 Demo（定义类的名称），（Hua在图形界面是第一级目录）
    "Hua": Demo
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {    #这是个字典，它将节点名称映射到人类容易读取的名字，可以通过 NODE_DISPLAY_NAME_MAPPINGS["Hua"] 访问到 "Demo Node" （第二级子目录）
    "Hua": "Demo Node"     # 一级目录名称hua，二级子目录名称Demo Node
}