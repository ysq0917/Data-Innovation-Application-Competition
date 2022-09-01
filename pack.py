from linebot.models import FlexSendMessage

def FM1_1():
    message = FlexSendMessage(
        alt_text = "老年年金給付與老年基本保證金",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "老年年金給付",
                        "size": "3xl",
                        "align": "center",
                        "weight": "bold",
                        "margin": "md",
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "請領資格",
                        "text": "老年年金給付請領資格"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "請領手續",
                        "text": "老年年金給付請領手續"
                        },
                        "style": "secondary",
                        "color": "#ECF5FF"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "給付核付",
                        "text": "老年年金給付核付"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "與勞保老年年金關係",
                        "text": "老年年金給付與勞保老年年金關係"
                        },
                        "style": "secondary",
                        "color": "#ECF5FF"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "老年基本保證金",
                        "size": "3xl",
                        "align": "center",
                        "margin": "md",
                        "weight": "bold",
                        "color": "#5599FF"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "請領資格",
                        "text": "老年基本保證金請領資格"
                        },
                        "style": "primary",
                        "color": "#9999FF"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "請領手續",
                        "text": "老年基本保證金請領手續"
                        },
                        "style": "secondary",
                        "color": "#E8CCFF"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "注意事項",
                        "text": "老年基本保證金注意事項"
                        },
                        "style": "primary",
                        "color": "#9999FF"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "給付核付",
                        "text": "老年基本保證金給付核付"
                        },
                        "style": "secondary",
                        "color": "#E8CCFF"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_2():
    message = FlexSendMessage(
        alt_text = "老年年金給付請領資格",
        contents = (
            {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "請領資格",
                    "color": "#FF0000",
                    "size": "3xl",
                    "align": "center",
                    "weight": "bold"
                }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "老年年金保險被保險人或曾參加老年年金保險者，於年滿65歲時，不論國保年資有幾年，均得請領老年年金給付。自符合條件（即年滿65歲）之當月起按月發給至死亡當月止。",
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                }
                ]
            }
            }
        )
    )

    return message

def FM1_3():
    message = FlexSendMessage(
        alt_text = "老年年金給付請領手續",
        contents = (
                {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "請領手續",
                            "size": "3xl",
                            "color": "#FF0000",
                            "weight": "bold",
                            "align": "center"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "※ 如年滿 65 歲當月月中還未收到通知函及申請書，可以直接在本網站下載列印 「國民年金老年年金給付申請書及給付收據 」，或親至勞保局各地辦事處索取。",
                            "size": "xl",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "點此進入官網下載",
                            "uri": "https://www.bli.gov.tw/0101306.html"
                            },
                            "style": "primary"
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "1.勞保局於每月月底均會針對次月即將年滿 65 歲而且符合請領條件者主動寄發通知函，並附上老年年金給付申請書表。如您年滿 65 歲時接獲通知函，請於申請書上填妥申請人姓名、出生日期、身分證統一編號、通訊地址以及匯入帳戶(金融機構帳戶或郵局帳戶請選擇一項勾填，勾選金融機構帳戶者必須是國內的帳戶)，並且簽名或蓋章。",
                            "size": "xl",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "2.在申請書指定的欄位貼妥要匯入給付之金融機構存簿封面 ( 要有戶名及帳號 ) 影本。",
                            "size": "xl",
                            "weight": "bold",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "3.將前述各項書表證件以掛號直接寄到勞工保險局國民年金組或送交到勞工保險局各地辦事處收件即可。",
                            "size": "xl",
                            "weight": "bold",
                            "wrap": True
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "4.另外，可使用自然人憑證申請老年年金給付，不必填寫申請書。操作步驟如下： 勞保局全球資訊網首頁／線上申辦／ e化服務系統(需自然人憑證) ／ 個人申報及查詢(依畫面指示登入系統) ／申辦作業 ─ 國民年金老年年金申辦(輸入各項欄位資料)，點選「申請」按鍵傳送資料，就完成申請國保老年年金給付的請領手續。 ",
                            "size": "xl",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "點此進入申報及查詢",
                            "uri": "https://edesk.bli.gov.tw/na/"
                            },
                            "style": "primary"
                        }
                        ]
                    }
                    }
                ]
                }
        )
    )
        
    return message

def FM1_4():
    message = FlexSendMessage(
        alt_text = "老年年金給付核付",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "給付核付",
                        "size": "3xl",
                        "color": "#FF0000",
                        "weight": "bold",
                        "align": "center"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "1.勞保局收到申請書件後，如經審查申請人符合老年年金給付請領條件而且申請手續都完備，會從申請人符合條件(也就是年滿65歲)的當月開始按月發給老年年金，一直到申請人死亡當月為止。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "2.當月應發給的老年年金，勞保局會在次月底前（ 最後一個工作日 ）匯到申請人指定的國內金融機構或郵局帳戶。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "3.領取老年年金給付的請求權，從符合請領之日起，因5年間不行使而消滅。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_5():
    message = FlexSendMessage(
        alt_text = "老年年金給付與勞保老年年金關係",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "與勞保老年年金關係",
                        "size": "xl",
                        "color": "#FF0000",
                        "weight": "bold",
                        "align": "center"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "1.被保險人年滿65歲時，如同時符合國保及勞保老年年金給付的請領資格，可以向勞保局同時申請國保及勞保的老年年金給付。國保和勞保的老年年金給付，必須分別依國民年金法和勞工保險條例的相關規定，各別計算保險年資及給付金額，再匯入被保險人帳戶。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "2.勞保年金制度實施後，勞保被保險人需勞保年資滿15年才能請領勞保老年年金給付。然而，勞工年滿65歲時如果勞保年資沒有達到15年，但經併計以往曾參加國保的年資後有滿15年以上，還是可以請領勞保老年年金給付。被保險人可備妥申請書件，向勞保局同時請領國保及勞保的老年年金給付，勞保局將依各該保險的規定，分別計算保險年資及給付金額後，再匯入被保險人帳戶。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請領手續",
                        "color": "#0080FF",
                        "size": "3xl"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "年滿65歲同時申請國保及勞保老年年金給付的被保險人，應下載列印「同時請領勞工保險、國民年金保險老年年金給付申請書及給付收據」，填妥相關欄位及要入帳的存簿封面(要有戶名及帳號)影本後，以掛號寄送勞保局或送交到勞保局各地辦事處收件。",
                        "size": "xl",
                        "weight": "bold",
                        "wrap": True
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "點此進入官網下載",
                        "uri": "https://www.bli.gov.tw/0101311.html"
                        },
                        "style": "primary"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_6():
    message = FlexSendMessage(
        alt_text = "老年基本保證金請領資格",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請領資格",
                        "wrap": True,
                        "weight": "bold",
                        "size": "3xl",
                        "color": "#FF0000",
                        "align": "center"
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "已年滿65歲之國民，即民國32年10月1日 （含當日）以前出生之國民，在國內設有戶籍，且最近3年內每年居住超過183日，而無下列規定之一者，得請領老年基本保證年金，自申請當月起按月發給3,772元（一）、經政府全額補助收容安置。",
                        "wrap": True,
                        "size": "xl",
                        "margin": "none",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "（二）、領取軍人退休俸（終身生活補助費）、政務人員、公教人員、公營事業人員月退休（職）金或一次退休（職、伍）金。但有下列情形之一者，不在此限：",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "1.軍人、政務人員、公教人員、公營事業人員領取一次退休（職、伍）金且未辦理政府優惠存款者，未領取公教人員保險養老給付或軍人保險退伍給付，或所領取公教人員保險養老給付、軍人保險退伍給付之總額，自年滿65歲當月起以新臺幣3,000元按月累計達原領取總額。",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "text",
                        "text": "2.原住民領取一次退休（職、伍）金。",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "（三）、領取社會福利津貼（指低收入老人生活津貼、中低收入老人生活津貼、身心障礙者生活補助、老年農民福利津貼及榮民就養給付）。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "（四）、財稅機關提供保險人公告年度之個人綜合所得稅各類所得總額合計達新臺幣50萬元以上。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "（五）、個人所有之土地及房屋價值合計達新臺幣500萬元以上。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "（六）、入獄服刑、因案羈押或拘禁。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_7():
    message = FlexSendMessage(
        alt_text = "老年基本保證金請領手續",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請領手續",
                        "wrap": True,
                        "weight": "bold",
                        "size": "3xl",
                        "color": "#FF0000",
                        "align": "center"
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "※「國民年金老年基本保證年金申請書及給付收據」及 「個人所有唯一房屋且實際居住切結書」除可直接在本站下載列印外，亦可到勞保局各地辦事處索取。",
                        "wrap": True,
                        "size": "xl",
                        "margin": "none",
                        "weight": "bold"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "點此進入官網下載",
                        "uri": "https://www.bli.gov.tw/0014264.html"
                        },
                        "style": "primary"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "一、下載列印「國民年金老年基本保證年金申請書及給付收據」後，於申請書上填妥申請人姓 名、出生日期、身分證統一編號、通訊地址以及匯入帳戶 ( 金融機構帳戶或郵局帳戶請選擇一項勾填，勾選金融機構帳戶者必須是申請書上限定之入帳銀行的帳戶 ) ，並且簽名或蓋章。",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "點此進入官網下載",
                        "uri": "https://www.bli.gov.tw/0014264.html"
                        },
                        "style": "primary"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "二、在申請書指定的欄位黏貼好要匯入給付之金融機構存簿封面（ 要有戶名及帳號 ）影本。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "三、如果是因「個人所有之土地及房屋價值合計達500萬元以上」，但符合下列扣除規定者，應同時檢具下列書件：",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "（一）、土地屬於尚未徵收及補償的公共設施保留地要扣除土地公告現值時：",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "請領人要另外再檢附縣 ( 市 ) 政府建管單位或鄉 ( 鎮、市、區 ) 公所出具的都市計畫土地使用分區證明或公共設施保留地證明，以及稅捐稽徵機關核發的個人「全國財產稅總歸戶財產查詢清單」。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "（二）、房屋是屬於個人所有之唯一房屋且實際居住者，要扣除房屋的評定標準價格及其土地的公告現值時：",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "請領人要另外再檢附稅捐稽徵機關核發的「全國財產稅總歸戶財產查詢清單」並填寫「個人所有唯一房屋且實際居住切結書」。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "（三）、土地屬於未產生經濟效益之原住民保留地，要扣除土地公告現值時：",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "請領人應書面主張其所有的土地是屬於未產生經濟效益的原住民保留地，並檢附稅捐稽徵機關核發的「全國財產稅總歸戶財產查詢清單」；",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "如果該筆未產生經濟效益的原住民保留地屬於都市計畫法的土地，請另外向縣（市）政府建管單位或權限下授之鄉（鎮、市、區）公所申請「土地使用分區證明書」。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "四、將前述各項書表證件以掛號直接寄到勞保局國民年金組或送交到勞保局各地辦事處收件即可。",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_8():
    message = FlexSendMessage(
        alt_text = "老年基本保證金注意事項",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "注意事項",
                        "wrap": True,
                        "weight": "bold",
                        "size": "3xl",
                        "color": "#FF0000",
                        "align": "center"
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "1.自101年1月起，原已領取老年基本保證年金的人，在各地方政府調整土地公告現值後，如其個人所有的土地及房屋沒有新增，而且也沒有其他排除規定，就符合繼續請領年金的資格，不會因為土地公告現值調整而受到影響。",
                        "wrap": True,
                        "size": "xl",
                        "margin": "lg",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "2.國民年金開辦後原本已經在領「敬老福利生活津貼」3,000元的人，於國民年金開辦後，由勞保局改以國民年金老年基本保證年金名義繼續發放，按月發給老年基本保證年金3,000元。另國民年金法於100年12月21日修正公布增列第54條之1，自101年1月起給付金額由3,000元調整為3,500元；自105年1月起調整為3,628元，109年1月起為3,772元。",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "3.國民年金法第31條第1項第2款第1目於100年6月29日修正公布，放寬領取軍公教人員一次退休金的人，如果沒有辦理政府優惠存款，可以從年滿65歲當月起按月累計3,000元，累計到達原已領取的退伍給付或公保養老給付領取總額，就可以請領老年基本保證年金。符合上述放寬條件，如果在修法前未曾向勞保局提出申請老年基本保證年金的人，",
                        "wrap": True,
                        "size": "xl",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "可以向勞保局提出申請，但在修法前曾經向勞保局提出申請者，則無須重新提出申請。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "4. 97年10月1日國民年金開辦時仍未滿65歲的人，已經不再適用敬老津貼，亦不能領老年基本保證年金。如符合國民年金加保資格，並依規定繳納保險費者，年滿65歲時，可以向勞保局申請老年年金。",
                        "size": "xl",
                        "wrap": True,
                        "weight": "bold"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM1_9():
    message = FlexSendMessage(
        alt_text = "老年基本保證金給付核付",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "給付核付",
                        "wrap": True,
                        "weight": "bold",
                        "size": "3xl",
                        "color": "#FF0000",
                        "align": "center"
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "1.勞保局收到申請書件後，如經審查申請人符合老年基本保證年金請領條件而且申請手續完備，會從申請人提出申請的當月開始按月發給3,772元，並在次月底前匯到申請人指定的國內金融機構或郵局帳戶，一直到申請人死亡當月為止。",
                        "wrap": True,
                        "size": "xl",
                        "margin": "lg",
                        "weight": "bold"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "2.請領人在領取老年基本保證年金期間，勞保局會每月定期比對各項社會保險、社會福利津貼、財稅等資料，如果比對後發現請領人有不符合請領資格的情形時，勞保局會發公文通知請領人暫停發給老年基本保證年金，等到以後比對如果又符合資格時，再恢復發給，請領人不必重新提出申請。",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_1():
    message = FlexSendMessage(
        alt_text = "老年年金給付與老年基本保證金",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "老年年金試算",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "條件",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "請領年齡為65歲，且保險年資需滿15年，辦理離職退保後才能領取老年年金。",
                        "weight": "bold",
                        "align": "center",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "勞工保險年資未滿15年，但併入國民年金保險之年資滿15年，於年滿65歲時，可選擇請領老年年金給付。",
                        "weight": "bold",
                        "align": "center",
                        "wrap": True
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "每月領取",
                        "text": "每月領取"
                        },
                        "style": "primary",
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "展延年金",
                        "text": "展延年金"
                        },
                        "style": "secondary",
                        "color": "#ECF5FF"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "勞工月退休金估算",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#5599FF"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "條件",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "1.勞工年滿60歲，工作年資滿15年以上者，得選擇請領退休金",
                        "weight": "bold",
                        "align": "center",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "2.工作年資以有實際提繳退休金之月數計算，年資中斷者，其前後提繳年資合併計算。",
                        "weight": "bold",
                        "align": "center",
                        "wrap": True
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "勞工月退休金",
                        "text": "勞工月退休金"
                        },
                        "style": "primary",
                        "color": "#9999FF",
                        "margin": "xxl"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_2():
    message = FlexSendMessage(
        alt_text = "選擇每月領取計算公式",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "每月領取",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "A式",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "平均月投保薪資×年資×0.775%+3,000 元",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "B式",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "平均月投保薪資×年資×1.55%",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "Hint",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "年資較長者(25年)，選擇第 2 式較有利，未滿30日算一個月",
                        "wrap": True
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "A式（A1）",
                        "text": "每月領取A式"
                        },
                        "style": "primary",
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "B式（B1）",
                        "text": "每月領取B式"
                        },
                        "style": "secondary",
                        "color": "#ECF5FF"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_3():
    message = FlexSendMessage(
        alt_text = "選擇展延年金計算公式",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "展延年金",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "A式",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "平均月投保薪資×年資×0.775%+3,000 元",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "B式",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "平均月投保薪資×年資×1.55%",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "Hint",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "年資較長者(25年)，選擇第 2 式較有利，未滿30日算一個月",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "延展時間最高5年!!!",
                        "wrap": True,
                        "color": "#0000FF"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "A式（A2）",
                        "text": "展延年金A式"
                        },
                        "style": "primary",
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "B式（B2）",
                        "text": "展延年金B式"
                        },
                        "style": "secondary",
                        "color": "#ECF5FF"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_4():
    message = FlexSendMessage(
        alt_text = "勞工月退休金",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "勞工月退休金",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "估算公式",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "text": "（個人專戶本金及累積收益總額／期初年金現值因子）／12",
                        "wrap": True,
                        "align": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "勞工月退休金金額估算（C）",
                        "text": "勞工月退休金金額估算"
                        },
                        "style": "primary",
                        "margin": "xxl"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_5(sample):
    message = FlexSendMessage(
        alt_text = "請依照範例輸入資訊!!!",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請輸入以下資訊",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "請輸入平均月投保薪資和年資(單位：年)",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "請依照範例輸入並根據自身情況修改薪資和年資!!!",
                        "wrap": True,
                        "align": "center",
                        "weight": "bold",
                        "color": "#0000FF"
                    },
                    {
                        "type": "text",
                        "text": "範例",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": sample
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM2_6(sample):
    message = FlexSendMessage(
        alt_text = "請依照範例輸入資訊!!!",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請輸入以下資訊",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "請輸入平均月投保薪資、年資(單位：年)和延展時間(單位：年)",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "請依照範例輸入並根據自身情況修改薪資、年資和延展時間!!!",
                        "wrap": True,
                        "align": "center",
                        "weight": "bold",
                        "color": "#0000FF"
                    },
                    {
                        "type": "text",
                        "text": "範例",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": sample
                    }
                    ]
                }
                }
            ]
            }
        )
    )
    
    return message

def FM2_7():
    message = FlexSendMessage(
        alt_text = "請依照範例輸入資訊!!!",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請輸入以下資訊",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "請輸入個人專戶本金及累積收益總額和預估請領年齡",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "預估請領年齡必須為60歲以上!!!",
                        "wrap": True,
                        "align": "center",
                        "weight": "bold",
                        "color": "#0000FF"
                    },
                    {
                        "type": "text",
                        "text": "請依照範例輸入並根據自身情況修改金額和年齡!!!",
                        "wrap": True,
                        "align": "center",
                        "weight": "bold",
                        "color": "#0000FF"
                    },
                    {
                        "type": "text",
                        "text": "範例",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "C 1000000 60"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM3_1():
    message = FlexSendMessage(
        alt_text = "請依照範例輸入資訊!!!",
        contents = (
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請輸入以下資訊",
                        "size": "xxl",
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "請輸入縣市區域和預算",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "請依照範例輸入並根據自身情況修改縣市區域和預算!!!",
                        "wrap": True,
                        "align": "center",
                        "weight": "bold",
                        "color": "#0000FF"
                    },
                    {
                        "type": "text",
                        "text": "範例",
                        "color": "#FF0000",
                        "size": "xl",
                        "weight": "bold",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "weight": "bold",
                        "align": "center",
                        "text": "D 高雄市大寮區 50000"
                    }
                    ]
                }
                }
            ]
            }
        )
    )

    return message

def FM3_2(address, money, df1):
    if "台" in address[:3]:
        city = "臺"+address[1:3]
    else:
        city = address[:3]
    region = address[3:]
    money = int(money)
    cnt = []
    for i in range(len(df1.address)):
        if df1.address[i][:3]==city and df1.region[i]==region:
            cnt.append(i)
    df2 = df1.iloc[cnt, [0, 3, 4]]
    result = df2[df2.money<=money].sort_values(by=["money"])
    name = list(result.name)
    phone = list(result.phone)
    money = list(result.money)
    n = len(result)
    if n<5:
        for i in range(5-n):
            name.append("無資料")
            phone.append("無資料")
            money.append("無資料")
    message = FlexSendMessage(
        alt_text = "推薦長照機構",
        contents = (
            {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "推薦長照機構",
                    "size": "3xl",
                    "weight": "bold",
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": name[0],
                        "align": "center",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "電話："+phone[0],
                            "color": "#111111",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "費用："+str(money[0])+"／月",
                            "color": "#111111",
                            "align": "end",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": name[1],
                        "align": "center",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "電話："+phone[1],
                            "color": "#111111",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "費用："+str(money[1])+"／月",
                            "color": "#111111",
                            "align": "end",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": name[2],
                        "align": "center",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "電話："+phone[2],
                            "color": "#111111",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "費用："+str(money[2])+"／月",
                            "color": "#111111",
                            "align": "end",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": name[3],
                        "align": "center",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "電話："+phone[3],
                            "color": "#111111",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "費用："+str(money[3])+"／月",
                            "color": "#111111",
                            "align": "end",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": name[4],
                        "align": "center",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "電話："+phone[4],
                            "color": "#111111",
                            "wrap": True,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "費用："+str(money[4])+"／月",
                            "color": "#111111",
                            "align": "end",
                            "wrap": True,
                            "weight": "bold"
                        }
                        ]
                    }
                    ],
                    "margin": "lg"
                }
                ]
            }
            }
        )
    )

    return message