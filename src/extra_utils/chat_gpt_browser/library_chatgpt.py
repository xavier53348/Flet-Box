import g4f
import asyncio
import os
import time

def ChatGpt(question="What's chat gpt"):
    _providers = [
                    # g4f.Provider.GeekGpt,              #*****
                    # g4f.Provider.HuggingChat,          #*****
                    # g4f.Provider.Aura,                 #*****

                    # g4f.Provider.GptGo,                #*****
                    # g4f.Provider.ChatForAi,            #***

                    # g4f.Provider.Llama2,               #****
                    g4f.Provider.Bing,                 #****
                    # g4f.Provider.ChatForAi,            #***
                    # g4f.Provider.ChatgptDemo,          #***
                    g4f.Provider.Liaobots,             # books
                    # g4f.Provider.ChatgptAi,            # books
                    # g4f.Provider.ChatBase,             #*
                 ]
    # _providers = [

                    # g4f.Provider.AItianhu,
                    # g4f.Provider.GptForLove,
                    # g4f.Provider.AItianhuSpace,
                    # g4f.Provider.Acytoo,
                    # g4f.Provider.GptGod,
                    # g4f.Provider.AiAsk,
                    # g4f.Provider.GptTalkRu,
                    # g4f.Provider.AiChatOnline,
                    # g4f.Provider.H2o,
                    # g4f.Provider.AiChatting,
                    # g4f.Provider.Hashnode,
                    # g4f.Provider.Aichat,
                    # g4f.Provider.AiService,
                    # g4f.Provider.Aibn,
                    # g4f.Provider.Koala,

                    # g4f.Provider.Komo,
                    # g4f.Provider.Ails,
                    # g4f.Provider.Aivvm,
                    # g4f.Provider.AsyncGeneratorProvider,


                    # g4f.Provider.Lockchat,
                    # g4f.Provider.AsyncProvider,
                    # g4f.Provider.MikuChat,
                    # g4f.Provider.MyShell,
                    # g4f.Provider.Bard,
                    # g4f.Provider.Myshell,
                    # g4f.Provider.BaseProvider,
                    # g4f.Provider.OnlineGpt,
                    # g4f.Provider.Berlin,
                    # g4f.Provider.Opchatgpts,
                    # g4f.Provider.OpenAssistant,
                    # g4f.Provider.ChatAiGpt,
                    # g4f.Provider.OpenaiChat,
                    # g4f.Provider.ChatAnywhere,
                    # g4f.Provider.PerplexityAi,
                    # g4f.Provider.Phind,
                    # g4f.Provider.Pi,
                    # g4f.Provider.Chatgpt4Online,
                    # g4f.Provider.Poe,
                    # g4f.Provider.ProviderUtils,
                    # g4f.Provider.Raycast,
                    # g4f.Provider.ChatgptDemoAi,
                    # g4f.Provider.RetryProvider,
                    # g4f.Provider.ChatgptDuo,
                    # g4f.Provider.TalkAi,

                    # g4f.Provider.ChatgptFree,
                    # g4f.Provider.Theb,
                    # g4f.Provider.ChatgptLogin,
                    # g4f.Provider.ThebApi,
                    # g4f.Provider.ChatgptNext,
                    # g4f.Provider.V50,
                    # g4f.Provider.ChatgptX,
                    # g4f.Provider.Vercel,
                    # g4f.Provider.Chatxyz,
                    # g4f.Provider.Vitalentum,
                    # g4f.Provider.CodeLinkAva,
                    # g4f.Provider.Wewordle,
                    # g4f.Provider.Cromicle,
                    # g4f.Provider.Wuguokai,
                    # g4f.Provider.DeepInfra,
                    # g4f.Provider.Ylokh,
                    # g4f.Provider.DfeHub,
                    # g4f.Provider.You,
                    # g4f.Provider.EasyChat,
                    # g4f.Provider.Yqcloud,
                    # g4f.Provider.Equing,
                    # g4f.Provider.annotations,
                    # g4f.Provider.FakeGpt,
                    # g4f.Provider.base_provider,
                    # g4f.Provider.FastGpt,
                    # g4f.Provider.deprecated,
                    # g4f.Provider.Forefront,
                    # g4f.Provider.helper,
                    # g4f.Provider.FreeGpt,
                    # g4f.Provider.needs_auth,
                    # g4f.Provider.GPTalk,
                    # g4f.Provider.retry_provider,
                    # g4f.Provider.selenium,
                    # g4f.Provider.GetGpt,
                    # g4f.Provider.sys,
                    # g4f.Provider.Gpt6,
                    # g4f.Provider.unfinished,
                    # g4f.Provider.GptChatly,
                      # ]

    async def run_provider(provider: g4f.Provider.BaseProvider,message):
        global response
        global check_check

        try:
            response = await g4f.ChatCompletion.create_async(
                model    = g4f.models.default,
                messages = [{"role": "user", "content": f"{message}"}],
                provider = provider,
            )

            if provider:
                check_check = True

        except Exception as e:
            print(f"{provider.__name__}:", e)
            check_check =  False

    async def run_all(message):
        global check_check
        # calls = [
        #             run_provider(provider,message) for provider in _providers
        #         ]
        calls = []
        check_check=True

        for provider in _providers:
            data = run_provider(provider,message)
            calls.append(data)

        for _ in calls:
            await asyncio.gather(_)
            # time.sleep(4)
            if check_check:
                calls =[]
            # print(check_check)
        # await asyncio.gather(*calls)

    data_tmp = asyncio.run(run_all(question))
    time.sleep(0.1)
    # tmp_response = {question:response}

    try:
        return response
    except Exception as e:
        return False

if __name__ == '__main__':
    data = ChatGpt(question='simple hello ')
    print(f"====>> {data}")