import re


def main():
    str = """<div class="content content-word">技能要求：<br>Matlibplot，算法和数据结构，分布式，区块链，嵌入式，网络爬虫<br>工作职责：1
    .完成公司策略系统和交易平台的设计开发，负责量化策略交易系统稳定运行；<br>2、完成量化策略统一历史回测系统的设计与开发，实现量化策略对接交易系统；； 
    <br>3、全流程参与特征工程、数据建模、模型训练、模型应用等相关工作，高质量完成项目开发并按时交付项目成果；<br>4、参与核心技术问题的解决，技术方案的制定和决策；<br>5
    、对量化交易系统以及策略的扩展、安全、性能、伸缩性、简洁性等做系统级的把握；<br>6、参与公司研发/项目流程建设。<br><br>任职资格：1、3年以上programming软件开发经验，2
    年以上的数据挖掘，策略和算法研发相关工作；<br>2、精通Python 熟悉Matlibplot、Pandas、Numpy、SciPy、等等；<br>3、编程基础扎实，熟悉算法和数据结构，有丰富的Python的工作经验；<br
    >4、熟悉数据库以及优化方法，熟悉MySQL、MongoBD、Redis数据库和多线程编程；<br>5、熟练掌握常用的Linux命令、了解shell脚本编程； 
    <br>6、熟悉常用机器学习和数据挖掘算法（如决策树、支持向量机、线性回归、逻辑回归和神经网络），并且有实际项目实施案例，具备相关的工程能力：<br>7、学习能力、责任感强，有较强的沟通能力。</div> """
    # str1 = re.sub(r'^<.+>$', "", str)
    # print(str1)
    print(re.sub(r"<[a-z A-Z0-9\"-=]*>", "", str))


if __name__ == '__main__':
    main()