class Example:   # 定义了一个名为 Example 的类,定义类的语法, 输出的规则
    """
    A example node 一个示例节点
 
    Class methods   类方法
    -------------
    INPUT_TYPES (dict): 输入_类
        Tell the main program input parameters of nodes.  告诉主程序输入节点参数
        
    IS_CHANGED:  已更改
        optional method to control when the node is re executed.  控制何时重新执行节点的可选方法。

    Attributes
    ----------
    RETURN_TYPES (`tuple`):   返回 类（元组）
        The type of each element in the output tulple. 输出元组中每个元素的类型

    RETURN_NAMES (`tuple`):   返回 名称
        Optional: The name of each output in the output tulple. 可选:输出元组中每个输出的名称。

    FUNCTION (`str`):         函数(str):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()  
        入口点方法的名称。例如，如果' FUNCTION = "execute" '，那么它将运行example ().execute()

    OUTPUT_NODE ([`bool`]):     输出_节点  （布尔）
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        如果此节点是输出节点，则从图中输出结果/图像。SaveImage节点就是一个例子。
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        后端在这些输出节点上迭代，如果它们的父节点图正确连接，则尝试执行它们的所有父节点。
        Assumed to be False if not present.
        如果不存在，则假定为False。


    CATEGORY (`str`):         类别
        The category the node should appear in the UI.
        类别节点应该出现在UI中。

    execute(s) -> tuple || None:   执行 - 元组  || 无
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        入口点方法。此方法的名称必须与属性' FUNCTION '的值相同。
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
        示例，如果' FUNCTION = "execute" '，那么这个方法的名字必须是' execute '，如果' FUNCTION = "foo" '，那么它的名字必须是' foo '。
    """
    def __init__(self):  #定义了一个特殊方法__init__() 方法会被自动调用，用于初始化新创建的对象。它是Python类中的构造函数
        pass
    
    @classmethod  #类方法
    def INPUT_TYPES(s): #定义@classsmethod名为INPUT_TYPES，返回输入字段配置的字典；输入的规则
        """
            Return a dictionary which contains config for all input fields.返回一个字典，其中包含所有输入字段的配置
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".部分类型(字符串):
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            输入类型“INT”，“字符串”或“浮动”是节点上字段的特殊值。
            The type can be a list for selection.类型可以是一个可供选择的列表。

            Returns: `dict`: 返回:“字典”: 意思就是图形界面返回到 代码模块变量里面
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                  键input_fields_group (' 字符串 '):可以是必需的，隐藏的或可选的。节点类必须具有属性“required”。
                - Value input_fields (`dict`): Contains input fields config:
                  数值 input_fields (' 字典 '):包含输入字段config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                      关键字段field_name (' 字符串 '): 入口点方法参数的名称
                    * Value field_config (`tuple`):  数值字段（元组）
                        + First value is a string indicate the type of field or a list for selection.
                           第一个值是一个字符串，表示字段的类型或可供选择的列表。
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
                          第二个值是类型为“INT”、“字符串”或“浮动”的配置。
        """
        return {    #返回
            "required": {     #要求
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value 最小值
                    "max": 4096, #Maximum value  最大值
                    "step": 64, #Slider's step  滑动的步骤
                    "display": "number" # Cosmetic only: display as "number" or "slider"仅用于修饰:显示为“数字”或“滑块”
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                                    #表示四舍五入精度的值将默认设置为步长值。可设置为False以禁用舍入。
                    "display": "number"}),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                                        #如果您希望该字段看起来像ClipTextEncode节点上的字段，则为True
                    "default": "Hello World!"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)      # 返回_类 这一个模块代码就是输出的对应节点了     
    #RETURN_NAMES = ("image_output_name",) 返回_名称=（图像_输出_名字）

    FUNCTION = "test"   #函数名称=test

    #OUTPUT_NODE = False   输出节点=假

    CATEGORY = "Example"   #类别 = 

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        #do some processing on the image, in this example I just invert it 对图像做一些处理，在这个例子中我只是把它倒过来
        image = 1.0 - image
        return (image,)

    """
        The node will always be re executed if any of the inputs change but
        如果输入中的任何一个发生了变化，节点将始终被重新执行
        this method can be used to force the node to execute again even when the inputs don't change.
        这个方法可以用来强制节点再次执行，即使输入没有改变。
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        您可以使该节点返回一个数字或字符串。该值将与节点最后一次返回的值进行比较
        executed, if it is different the node will be executed again.执行，如果不一致，将重新执行该节点。
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        该方法在LoadImage节点的核心repo中使用，如果图像哈希值为字符串，则返回图像哈希值
        changes between executions the LoadImage node is executed again.在执行之间更改LoadImage节点将再次执行。
    """
    #@classmethod  类方法
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):  函数要改变了这些括号的值
    #    return ""  返回

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# 设置web目录，该目录下的任何.js文件都将被前端作为前端扩展加载
# WEB_DIRECTORY = "./somejs"   web_目录

# A dictionary that contains all nodes you want to export with their names
# 包含要导出的所有节点及其名称的字典
# NOTE: names should be globally unique  注意:名称应该是全局唯一的
NODE_CLASS_MAPPINGS = {   #这段代码定义字典变量，将节点名称映射到相应的类，将字符串Example映射到Example，（在图形界面是第一级目录）
    "Example": Example
}

# A dictionary that contains the friendly/humanly readable titles for the nodes  包含节点的友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {    #这是个字典，它将节点名称映射到人类容易读取的名字，可以通过 NODE_DISPLAY_NAME_MAPPINGS["Example"] 访问到 "Example Node" （第二级子目录）
    "Example": "Example Node"
}
 