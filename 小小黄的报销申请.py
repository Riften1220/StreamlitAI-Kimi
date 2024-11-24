from openai import OpenAI
import streamlit as st


st.title("💬让我们来探索一下汇联易AI吧")


st.caption("🚀财务中心AI探索，接入kimi的API")

def char_by_char_yield(text):
    for char in text:
        yield char

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "你是一个费用报销审核专家，你可以提取合同关键字，总结信息，提示异常点，你也可以回答其他任何问题。"}]

content = "公司的报销规定为：必须以人民币报销。出差不得多于10天，否则就是可能在外面玩。节假日出差不算出差，不能报销。现在是2024年11月，只能报销1年以内发生的费用。报销金额不能超过5000元。具体报销单信息如下。出差人：小小黄，收款方：小小黄，出差日期：2022-01-01，出差时长：15天，出差地点：旧金山，开户支行: 中国工商银行股份有限公司北京幸福街支行，银行账号：1234567890，出差事由：参加国际人工智能大会，利润中心编码：P260000000，费用类型：飞机。货币：美元。报销金额：6999元。"

st.header("公司报销规定（假设）")
st.write('''假设公司的报销规定为：''')
st.write('1. 必须以人民币报销。')
st.write('2. 出差不得多于10天，否则就是可能在外面玩。')
st.write('3. 节假日出差不算出差，不能报销。')
st.write('4. 现在是2024年11月，只能报销1年以内发生的费用。')
st.write('5. 报销金额不能超过5000元。')
st.divider()
st.header("具体报销单信息")
st.write("出差人：小小黄")
st.write("收款方：小小黄")
st.write("出差日期：2022-01-01")
st.write("出差时长：15天")
st.write("出差地点：旧金山")
st.write("开户支行: 中国工商银行股份有限公司北京幸福街支行")
st.write("银行账号：1234567890")
st.write("出差事由：参加国际人工智能大会")
st.write("利润中心编码：P260000000")
st.write("费用类型：飞机")
st.write("货币：美元")
st.write("报销金额：6999元")
st.divider()
st.write("👇🏻我可以提取合同关键字，总结信息，提示异常点，任何问题都可以问我")


for msg in st.session_state.messages:
    if msg != st.session_state.messages[0]:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])

if st.button("提示风险点"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages"].append({"role": "user", "content": content+"就这份报销单而言，请提示风险点。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages"].append({"role": "assistant", "content": full_stream})

if st.button("请帮我总结"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages"].append({"role": "user", "content": content+"就这份报销单而言，请总结收款方、出差事由、报销金额。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages"].append({"role": "assistant", "content": full_stream})

if st.button("请帮我决策"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages"].append({"role": "user", "content": content+"就这份报销单而言，能报销吗？"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages"].append({"role": "assistant", "content": full_stream})

if prompt := st.chat_input('有任何问题都可以在这里向Kimi提问'):

    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages"].append({"role": "user", "content": content+prompt})
    st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages"].append({"role": "assistant", "content": full_stream})
