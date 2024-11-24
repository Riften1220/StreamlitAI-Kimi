from openai import OpenAI
import streamlit as st


st.title("💬让我们来探索一下汇联易AI吧")


st.caption("🚀财务中心AI探索，接入kimi的API")

def char_by_char_yield(text):
    for char in text:
        yield char

if "messages3" not in st.session_state:
    st.session_state["messages3"] = [{"role": "system", "content": "你是一个费用报销审核专家，你可以提取合同关键字，总结信息，提示异常点，你也可以回答其他任何问题。"}]

content = "公司的借款规定为：必须以人民币借款。借款款项必须用于中国境内。借款时间不得多于10天。借款金额不能超过50000元。如果借款项目为税金，必须是增值税或企业所得税。具体借款单信息如下。借款人：阿峰，收款方：阿峰，借款日期：2024-01-01，借款时长：25天，支付地点：旧金山，开户支行: 中国工商银行股份有限公司北京幸福街支行，银行账号：1234567890，借款事由：支付杰森吴个人所得税、车船税，利润中心编码：P260000000，费用类型：税金。货币：美元。借款金额：69999元。"

st.header("公司借款规定（假设）")
st.write('''假设公司的借款规定为：''')
st.write('1. 必须以人民币借款。')
st.write('2. 借款款项必须用于中国境内。')
st.write('3. 借款时间不得多于10天。')
st.write('4. 借款金额不能超过50000元。')
st.write('5. 如果借款项目为税金，必须是增值税或企业所得税。')
st.divider()
st.header("具体借款单信息")
st.write("借款人：阿峰")
st.write("收款方：阿峰")
st.write("借款日期：2024-01-01")
st.write("借款时长：25天")
st.write("支付地点：旧金山")
st.write("开户支行: 中国工商银行股份有限公司北京幸福街支行")
st.write("银行账号：1234567890")
st.write("借款事由：支付杰森吴个人所得税、车船税")
st.write("利润中心编码：P260000000")
st.write("费用类型：税金")
st.write("货币：美元")
st.write("借款金额：69999元。")
st.divider()
st.write("👇🏻我可以提取合同关键字，总结信息，提示异常点，任何问题都可以问我")

for msg in st.session_state["messages3"]:
    if msg != st.session_state["messages3"][0]:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])

if st.button("提示风险点"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages3"].append({"role": "user", "content": content+"就这份借款单而言，请提示风险点。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages3"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages3"].append({"role": "assistant", "content": full_stream})

if st.button("请帮我总结"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages3"].append({"role": "user", "content": content+"就这份借款单而言，请总结收款方、借款事由、借款金额。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages3"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages3"].append({"role": "assistant", "content": full_stream})

if st.button("请帮我决策"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages3"].append({"role": "user", "content": content+"就这份借款单而言，根据公司规定能借款吗？"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages3"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages3"].append({"role": "assistant", "content": full_stream})

if prompt := st.chat_input('有任何问题都可以在这里向Kimi提问'):

    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages3"].append({"role": "user", "content": content+prompt})
    st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages3"],temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages3"].append({"role": "assistant", "content": full_stream})
