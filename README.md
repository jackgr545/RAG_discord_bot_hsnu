# 師大附中校園導覽機器人

這是一個專為 **師大附中** 設計的校園導覽 Discord 機器人，使用 Python 開發，整合多種 API 並搭配 Gemini 語言模型，提供互動式語言生成與即時導航功能。


[架構簡圖](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=drawio_xml_flowchart.txt&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Python%20Functions%20Flowchart%22%20id%3D%22flowchart%22%3E1Zxbc9o4GIZ%2FjWd2bzo%2BHy5tbAhNk6YhbZLeMC4WwbuAGWNy6K9fnQzYUhNtApKZyUxlYTsvjz99J6vRrN7ieVCmq9lFkYG5ZurZs2bFmmkalunCf9DMC5nxXItMPJR5Rk%2FaTYzy34BO6nR2k2dg3TixKop5la%2Bak5NiuQSTqjGXlmXx1DxtWsybv3WVPgBmYjRJ5%2BzsbZ5VMzLrm95u%2FgzkD7P6NxtuQD5ZpPXJ9JusZ2lWPO1NWYlm9cqiqMho8dwDcwSv5kKu6%2F%2Fh062wEiwrkQtCcsFjOt%2FQ76Ylnhb6mh9piaNFPc3vo0EAf%2FAAzsMx0V691EDgTSF7eBA9zfIKjFbpBH3yBB8%2FnJtVizk8MuBwms%2FnvWJelPg6CxhTZ4ouY3XTr%2FIIygo8703R7zEAxQJU5Qs8hX5quZQpNSqbHj7tnpBRY5%2FtPZ36spQaxcP2zjtucEDR8TFGHIw%2BphdgaI4WOghsYGqRjmZCU%2FMtdE6YaH6oJS6iGvnwHp%2FA8pHhWxabZQYyCvENxkdgaciE2ePAhAx9LYgxOo8ap9%2FTAuhI9DhfT4oyg6MILpuuoZNqhzGD7ldRfSo3SzjJWcbQ7MKAzgQBWvaJrUUh%2BukaRksmxoRjgRBMrEV9vIptjAo6SR0tbbLS4eLdrXQXGafv4asiLbRZnLNi8Wuz%2Ft8Oc2oBZ%2BocCLHdcpg8xC4HsX8AxH0WsdlP1%2F9iQ30bn2Rr9JukHJ9DSj%2BSMQ54pB6K4mEOxmuQlpNZN5ltc5zXoB1rBZ9xzWtVZN1kZak0sOErBraAX%2FbwxNpObTrJMvMwJB2VVveZEzdgZDVQfEDBoa%2BFESpfwBKUaQX%2B%2BltDlZAFyxorWsAqCV7zz2Zdja%2FDgXKTbFmkK9Mizz%2FOseUgO%2BYLuTSPZZVfxGhi74iOPZTpbIu%2FHVl6Msy50YeJFniX4SjE6Y%2BFfYOLPgsC5bTb3lSq7V5waPuoaAktTAhy01ESGcGxhQfwI5yBw6w7dOsBxgmzzI%2FilOhqpRr1FYu5r6NSBibnkY1jFqwTY5yoe8jAUc0IU%2FdQ8%2B0B9g3wnIt0tUacI2jYxl7jI0CGTIpMUm2eyiPwZD6CS%2BYR1A6Z40ZYyodlCgsj%2FUC%2BWm8y9XWJTL9%2BPPIt03U6Jqlux%2Fww1zqP5Ye%2FcUhCjxqi1hvyw31aqENjDI29cKdjjAy6DtTrbcMMTEHDPES9fi1mmOvNYpGW%2Be9t5sVJKBRbZavrYeiuxPU9EsP4a5PPs%2FGqLBarqoMI25Yol%2BENhyFOlALSY9c13yWZqYMq1TCgmSlKUT3coSODAM90L3tt996lwv3OwCULeUwKqg4aY3s9GzJx%2FeCu52aVRNNNZGAwQ8XrPNJpPgpzokCv64Je51iaMlnecljSZvsALPJljoH52Pj2yZ0aVEsm1DsGaglvkYNHMK6K1fjfDi5oJrpIXdH3f7bCEfxOYDkBN2W6XE%2BLcgHKuoAnVaaJw%2Fg2ufRR7IGTnQMqdVn%2FZID2w%2BFohPMeHaU%2BCQ7EpEZsLebOkZO6dkPe7gxILUKODa1bE%2BUuiFoPvYpEZhrh95AwFfIwR9rwOMeFToIc4y4Vwp38yO0eY1sm44i3dcPBaPC2DNz%2FQf149AqkT3t3IX5LTtZ3kHSPoCOTYI%2B3XwMHYd%2Bmi9z3G1YaYdM9JaBSW5txzF%2F2jSKRZkSmHl4NaYAKsAdF%2B2T0PTeBF7t%2F2C4y8KcO8I%2FEWmoPM%2BFt9Wi72HDI4UnsOHS3u48OyHc6nfrgWLbsS23TGwxfOMyztALjSQG55Us4XGuoXx%2Fg1Y9L8jCmO%2BdO9FWIXMYmw3gyT8t8%2BjLOwLpChPNiSRjTTDbEPiPqozhHcJNXUNBFR%2FhJRNGH%2FbBE3IFU3BaDe5ovs33W43kxwQON7J3YNpuhUUcJTdTCZJuf7aE%2FWZM3dKkPwWYewgOoxhBOBTS617EZLxvv%2FEjYPBm0hlS0Dgcted00hua9KdP5GG%2FAZx0Km4SgMi7BLsZFPYaTIW5KJe5ykhA2g96jCQ9hcci2unbVnYOceuCdDnFLJvEBZ1Mlp7IWIX7UNPCIvG2p2zE5%2BzERwgjt1SBGG239RUwLwcjAUTBGDTbixiOylwY6F9zkQFsS1e%2FdZMhKTf6GnN2bqKDeJtAJ3qJuo74Q6o6TAWbtk3555zbDukYLqCdz7z%2FIHgDnv1HRqXWxKSeUC%2B3OVWkJUw8yRb8%2Buser37QEc5gfPoLGvT%2Bq2hRSHbGqeypVW0Kqe6zqWKVqW0h1zKpOVKp2hFQnrOq%2BStXue1UPVKr23qv6TKVq%2F72qhypVB0Kq%2B6zqzypV12HuDdkDVva5Utli0fGMlf1FqWyx8DhkZV8olS0WHy9Y2VdKZYsFyM%2Bs7EulssUi5HnXZIuFyC%2Bs7K9KZYvFyK9doy0WJC9Z2d%2BUyhaLkt9Y2dcqZZtiUZIje6RUtliU5Mi%2BUSpbLEpes7K%2FK5UtFiW%2Fs7J%2FKJUtFiV%2FsLJvlcoWi5IjVvadUtliUfKOlX2vVLZYlLxnZf9UKlssSv5kZdfb3hTpFguTIa%2F7p7T9Z4kFyltWd%2B%2FgDUB8aViW6cveCasiX1brvTtfoQlt2%2Fc1mJ1AtELeQSC33CHZahOnJBaXI16bVG2fVCwy33T28dpMW%2F8Yj1ewnczrJ8dKH69gRzlmhSdKe8qWWDJwxequ94Yp0i2WDdQiG8JNpcLF8oFaZEO4pVS4WEZQi2wIt5UKF0sJapEN4Y5K4bZYSlCLbAh3lQoXi9K1yMZLH6VvfWyxKJ3w3vsoffFjiwXOAedthGLhYoHzjPM%2BYnjwl1bvSoxcr5UYBUdIjGzOH219zqs7ONQ%2FoT9QgI7u0REdx8%2F7By%2F0QIh1V7l6VoPrmxfY%2BivPgb3aNVu%2FzmhtRyGM6GWv6HAMvo7tjYgRMzd62zTg4e5vC5PTd3%2Bh2Ur%2BAw%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
[google_map功能簡圖](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=google_map_flowchart%20(1).txt&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Google%20Map%20Command%20Flow%22%20id%3D%22google-map-flow%22%3E7R1Zb%2BM2%2BtcITR4m0H08Sj6mBVqg6AC7O%2FtiKDZtqyNLXkmeJP31y4%2BkLpKyZUeyk5lMgUaiJF7ffdGKMdk9f87C%2FfaPdIViRVdXz4oxVXTd0138f2h4oQ2WzRo2WbSiTVrd8CX6B7FGlbUeohXKWy8WaRoX0b7duEyTBC2LVluYZelT%2B7V1GrdH3YcbJDR8WYax2PrvaFVsWatme%2FWDX1G02bKhXd2hDx7D5bdNlh4SNl6SJog%2B2YVlN2yN%2BTZcpU%2BtpnAV7ovoO5qkcZqxJYSHIoWnxkwxJlmaFvRq9zxBMex5uZ%2B0i3nH02pBGUqKPh9kaInwTBb4i3CX06%2B%2Fh%2FGBbZAysxV3pvgWXHimEtjKzFLcueIapMVSAleZzZVgoni%2BotsxHjR4zPDVBq6Uma64quJDr8oMfz5VfHzhwMuuyVrcKbTAoxl%2B7S4OC0WfxGlyf6o%2FG2YRGGRGMyUISH%2Be4gbQ4k2UQIX%2B6puZBy95M9KisnF9Vwk02B%2F42IXecb94JgFZMqwUP8Lv4DWq9wyixUuJQAQFEOyliqf3tI0K9GUfLuHpE6YY3LYtdjG%2B0%2FDlOopjAnLyrYGMpavCZ3mRpd9Q%2BSQGdPu0CrNvd%2FilQPUs%2FJI%2BgRXrxkp7dHXvHjpLk6LRmUr%2BwRYJCMBw4jvKCvTcaGII8RmlO1RkL%2FgV9tS06BeMqDWboe1TTSK6ytq2Teoo0Zuh9KbquUZAfMFwUI6PK7RG2SJD%2BT5NciTg4zTKl2m2IuC3AJqAkBjkmhLoBKwUvhhwjuJ6IgKFT2FUwHBJgbJwWURp8lAO9kDGvhsYyNrKQo4AZPzEsx0jtEeBWAWJUxCzB4AYnniOFssUg0XGP1zFx0RGucUMyA7g5kMj0JmreBIoYRYQFYcVomiPWcGG3aqk116s5CHfx1Fx9wvu45dhQboKkbteykBqL130uB4FpMY1QYoFZLzYoGJB5LMcqD6wRNh%2BE6CIRXn5%2Bp2Ub2MWrZe82iLyhAkNyu4BzMmGsTnoNQAeXEO3YuEi54ZPikEBvFbhPymAyT%2FgI5hLJ7htiYCR4AYAbIT3zWcPdtFqBXMhfHoe7qIYAPkrir8jeI89YBqRpnMMHXOi8ED2cHhMMr0rYhLGmmgVFkf4g6f4nuI5BKemwLNF%2FgAXKmALPJqAQBYQrD1OlODLfGBO3gMrBgCWUarGL22Z2gCWZo1F9rB3C7KVi%2BUWLb9JwNUDONAyJSzfAU0Nv89ofS7CY5vuHg%2F5%2BbAIV04oZcGPpm2p5jgUOgR4zTZ4NQl8vZFUKwpehM2mTMrSMT%2F3zIYSJYIaK1oTxZ8z%2Fu%2Bb5ALrzD7RuDR41E1x2vlQXi%2FxPxmU1%2BvhtF2e4ky9J8mZQ8AkDrNo%2FbLAVnAhAMX%2FjUlDMD4CxiH9%2BTH5KDDG5gDAFrHCm8slNFGg2jL9M9pFSQRL3EfDasX2GsNQBllz5ZnkySYO85x1fjVpu8nCVYTqJ8SsHwTLLL0thfvy9SEI%2F5%2FP7k7%2Fa2nNw8%2B%2F24tP%2F11%2BfV5%2B0gWAotUGfWG3aVZs002ahPGsbg3aIK%2Ff%2BT1N9wzQf6OieGEbTVwaLTRAz1HxH%2Fj8wWJ3XxtPps%2BsZ3LzUt4keLmNj%2BD2a%2FNZ%2FRm5K7%2FrBFqeHrIlKrezWOBVFUzJLcIMt7BHu3CfLyrMh905CugMgdnyve1Zeg3YuLm1uLUDOjA1ebHE9WzCvx3GHALCFqDFADu4YtIC0VcjyDlC29eCxTd1A2EdLZidUNJPWXjtzvGHGlMh8Gr8AFhPmm5isPj%2BwFDAf%2Fw%2Ff3uH2pztndbm3JGofh0lK8L2F3G6JIxfgkcDg7Uak4maaug%2BCOaX%2BkdALDww%2FOnHD3%2FnMPnj31MnkEuWRNHehnmDP4%2BqNlrD9qR4Zlwbo96T1WhxalFlIl4DdwnargEYnYZIhbAYli5BzyOYewP7YwgQWJwPSLuesUAgkKQMCr3shQoi1JE%2B7QcawaZ4fxaEZfawIPSRLAhOTWnASCpCBRUAPn9YRRlaHrENOEY9JUwUA0wD4FFx4GtH3DPtHi5TXq5rfuyxdjvB%2B1FkYZQUf6UFlaC0u6Zt0mEy5NtwD3OpOcweZRGGLvD9svXPumkIPHTU084FzZHgoaaOZmWI9Nw0M7jNYmFe2MegTfavszUMo2FtqA%2Bqo%2Fe0OFr2Rm1%2BdFgcbWyqpfHAYl%2FrFPtx%2BIjioApNiy%2BgZOVD2BwmAzgcLdnaG5jY33giwy1eUG6I1tM%2BS5coz5sGzHAWFPkULyR8abywTzGh5o2e%2F4SGmjpcx24rNKbKoTftsUb2amq98J%2BsdJEflmTdXWqLjNP5JM4M3NBncXUsNmmkDLdgteXDf1qxOON2KhEFcH%2F%2FaR9Q%2FwDaj6PfUPuRCh3jTQidSxxczlkerncqb3rJFon8aIoXKdw1900IGo9z%2Blgel4LFvW84R99%2FtWCSbCXHuTwPMrnAOFMV90JfopCaNS9FGFXxK7OBBnyxLFPv8gLt85MGBx3SJeHEGQsVw7Sm0BfYldSP5UGGAbQQB9BJEwSzam%2FekrV1hsGEzNgj75MwZkDSDn5Ub1HJCTHaRPsccbYKa23aKmG%2Bp9mY6%2BgZ1j%2BEGPE0LodJ5m%2B6aoTEEP2DVxcjLbulFCknxIj2U1gtvaTIBiUog7SQRiLTDcRI%2F4iPOF0u7MOzLRe4MlYdwalSpueC%2F3zGtM1gKgv7sGGSsDhkYXwsb0vI3%2B2IELe8QFj7dYPTQR8sRny15ZXH%2FN03yxbnfLEjY%2BuQwkszgm3iebRB5YY%2BibfKswZl6z9fYNtW23zbtkyRb9sj8W0IYEbJKk0z%2FGedSimG9zVegmXcOF0pjsEMUF8IXFEdZkZiUeU0JN%2FTqBpJkQy0coYuUchocqs7slv0LekkQximHoeZMsN0LMyUe0NFZvMuNAr1wXXctlbhUR%2Fqj6dXkEVc5A4lwe9SJ1js01zUN2QC%2FsbWqsOlBzuOOaj12bErvFoTkNh9GfsXC4MoL%2FSJ%2FMbsE9t%2F8uSD5khRv8wDoWe4cIn9S8w%2B32ZGoU9miGdFGTnWM7x5LUbOtmJl%2BQlQ0UKUOTy665VT8thMPE3gHx%2F8vpPfO8YVNZHDnqSfb6McM%2BwXCY7bBMcrLKOqu0ZyZy3APt9jOIJRj7qFsbIqpnNuw6IeBM87IP2rDdJxoatAa%2Bg3ROMJJOk6RbOLYXGrR5HMOo72v7LO4fpf7BrLvSKMktPM9%2BISCOuaJRByTeAN%2BBYuclF%2F%2BBZKcZ8jIm6ahYonXQtlyGNgmS8IdY0X6jyLozNlX9W4fK7yIIwzsOtasse84uCRxFHiq8XsVFfbFaJVKA4CbxKrS1YPuk7jOH067B9g9M5qtglwV6YgBL1LoBvOGZeE%2FM52cfTxU5%2FURDxSiueAPArUsV0it6iAtW1R9ks5%2FCCpL0DOovi8hNH24jxyb7Un8iBZcf%2B1WU8V%2Bi27oCsRWM8F3AGWovfaMdlGNDdKVnV%2BffcvjGj0Wo9svq3sG6Em%2BzarMXutRpxtcy2yYuTbrEbivblQL%2Bq1LbKFNzdGWls7NnmbXI6h1ZO8hY4qq6vkE9o4Kgo%2FTjnhvvMyjPPeL9cxlAoEALV74YsUH1qUJK%2FvvQ0xOb3WRFMMk7RrMY1srNsswz1jGS8o165DpRVVdgnhgYjLdOXCfkjk93rtsFhI20SWrlqo2%2BBMyen6%2BJMlk24rLrJCmRstS3L41BGS1jtWwxWd3GgtbHZSWf%2Bgt9L0tEuFfTsyUIyYKy16%2FTkxXiXNnivG%2BY4M3mU2EKfpqm3onBeXKMy9Pwhn0vop61yFTstA68oZvxHW99PXSwqWpP0LOdI3WkhPoXFCw5Y59W%2BzIL2fyJBNuLkgiT%2FtRus5wl%2B1QZhrC868rng9%2B7LDaOC4mct7oXpbUVa7I2ckK8rgFD3LGp6dymIi4%2BGETNe4OVrYHFrwJRJ90cLkjFLHGActbN4bMAZaSKo5XhPCGh6VBKF3azxyuNp961LtTjflzpPBtTveSTMwHsVog6RV7FUQxYTkPTcoC7F8lgQCoZru0M5cZUkgEFmxwx0EQpLHfE9CLqQSgWae%2Bg7Jh53XIRrofUqqII50CuEsEiCasOQYlicrFGwc6wQz1VZMjB6PUabY4NV3fmzCXOsUX%2FraKvouec9mXeN98GjXQXlU8ImkHQhNeWTD2eRsFojypyxJpn0Eb9lDvg%2BTFlOw%2F3dISYYEjS9Bf42TdLPN4x07Rbf8c0%2F%2FwhMdDlqAm%2BbF%2FT2h%2F8ZRz58afRdZmOQlXwjq4at18fjA5o2xgE69eq179%2FF20aJ9VXbi5pEPTRk2ike3ybGoCWEMHH9CkOT0xvfbJ3Vo%2BAgbX%2Be9eFBiyZK2SB5ZdWL1cWDg5uYmdLRyMulViVgW%2FCdNluETsWK0LiT5EkW6HyaOyhev2aWCeaoMRxstV8YU%2BXZ%2FpV%2Fwdjdlc9u7PLZU5nVoIbuor1TmOzJ466FDKl8iOFs7xItOkhvJEwJGtKKN7f2zfbBpGv0TPpKugIyY3oD7tQLFmkJfhyLNWdqPQDAsbapJXWVTI1toqHMjubJNwxNTDgwJofAq1GB0Yo1MJ9cLX5hCLaB9GaXwpy5q5YlKI8dBuF9deL3%2BygGAzyx1ZUev%2FiyEaHKEWB1xcytCtC8jRHksRyav9OuQIW%2Fdm5d6qQQ3Qc8gwSsElv4hscRzyjguZUpKrK9KKM5lhNIZNZHRinEdWuE9GBfTCt%2BRU%2Fq%2FxqMV44NWxGISm9Oxb63daaIb9CbHMfeiUPkKJGHvUY8Je91%2By1QtvgIe%2FLq7cL84ZPHdfUf5eVXB65NE8ZOnigxew9VGk%2FdU0eUZnGYnOxNEdrTUeL4ISZr3Tet21KPE2nm01Km4x49cuHP00I8rh27OjsPyAZkTaTAaVxNpDZwGc3QvuVIdzO7Yyb8qKYQVDiqhRTHU%2Fc%2F%2FYp9QJkPDMnD8LDlumBXplr9cwn5sqhlumRE%2F9nWZ7Zs4WYnPUJbVxlyXi%2Bpdiv8N2arWZKr9D0awNK%2FJV9UHD6sAPyRvvfxghDPstfow2bENNpdzDQqJi30NNuHgMj5pYyAfI39%2BrTF0jJwDwIePscFDXS4zR5dUkF%2FVHNQlMlZgoTWbslWTY1POqRqly%2Bm9ryMT49q1PJn8r2leSuxCWvGV0p1HI3aZn%2FRnJ3bbfWvE7t1OPWrwENdp8ZBL%2BMc71X16sb0TRxa%2FwbOfzj2p2NHk56iMak0akrLb93FomudytoFan6L2QTQlDktOcLwe2bzugGBPIjzL%2FDzqA6ZJkN6cHCtW%2FmAOyIn5hvw6D3iPFb15BAfJnZT8EEDtQjjls3id27YD1ozM2iQluEFc%2FdG44NywkpZl50hZyF2ZAynxfPhTkOpSN8hox0GWE2jp8M0syzqjEU4PndRxha78xQ%2BcGRpnTP6EI4nzTPYreKZzNtLg2yyFXNZaemJAbf9IVwje%2BD8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)


## 功能簡介

- 使用 [Gemini API](https://aistudio.google.com/apikey) 進行自然語言生成，根據使用者輸入提供智能回應。
- 整合 [SerpAPI](https://serpapi.com/)，可在 Discord 中直接搜尋 Google 網頁內容。
- 利用 [Google Maps Direction_API](https://developers.google.com/maps/documentation/directions/?hl=zh_TW) 提供即時的路線規劃與導航服務。
- 額外支援 [NASA API](https://api.nasa.gov/)，每日推送美麗的星空照片，讓校園導覽增添一點浪漫氛圍。  
  > （雖然跟校園導覽無關，但增添趣味與氣氛！）



## 安裝方式

### 方式一：使用 Git 克隆專案

1. 在任意位置建立一個新資料夾，並用 VSCode 開啟終端機 (Terminal)。
2. 輸入以下指令下載專案：

    ```bash
    git clone https://github.com/jackgr545/RAG_discord_bot_hsnu.git
    cd RAG_discord_bot_hsnu
    ```

3. 確認你的 Python 版本為 3.10（建議使用虛擬環境，避免版本衝突）。
4. 安裝專案所需套件：

    ```bash
    pip install -r requirements.txt
    ```

5. 將 `example.env` 複製並重新命名為 `.env`，並依說明設定你的 API 金鑰。



### 方式二：手動下載 ZIP 檔

1. 在 GitHub 專案頁面點選「Code」按鈕，選擇「Download ZIP」下載專案壓縮檔。![螢幕擷取畫面 2025-06-02 172622](https://github.com/user-attachments/assets/50767b45-94d0-407f-ae28-b5d03bc4950c)

2. 將 ZIP 檔解壓縮後，將裡面所有檔案拖曳到你新建立的資料夾中。

3. 進入資料夾，確認 Python 版本為 3.10（建議使用虛擬環境，避免版本衝突），並安裝需求套件：

    ```bash
    pip install -r requirements.txt
    ```

4. 將 `example.env` 複製並重新命名為 `.env`，並依說明設定你的 API 金鑰。



## API 金鑰與環境變數設定

### DISCORD_TOKEN
1. 前往[DISCORD.DEV](https://discord.com/developers/applications)，點選右上角的New Application
   
   ![螢幕擷取畫面 2025-06-02 175737](https://github.com/user-attachments/assets/7d9db1a4-a064-4433-b796-e44fd0a703ea)
   
2. 幫機器人命名，並確保OAuth2 URL Generator下的bot跟bot permittion administrator有被勾選
   
  ![螢幕擷取畫面 2025-06-02 193631](https://github.com/user-attachments/assets/0f090ffc-fc99-4a9f-8ae7-469dad2a4e2f)
  
  ![螢幕擷取畫面 2025-06-02 193753](https://github.com/user-attachments/assets/09c7114d-7a80-49ec-bdf2-579f9b5c641b)
3. 複製Generated URL，貼到google的網址欄，即可邀請bot加入你的伺服器
   
  ![螢幕擷取畫面 2025-06-02 200857](https://github.com/user-attachments/assets/1ce2a407-1dba-45ff-ad77-d68e99dabe54)
  
4. 切到bot類別下，把你能打開的選項都打開
   
  ![螢幕擷取畫面 2025-06-02 201831](https://github.com/user-attachments/assets/706b6541-08df-4f6e-a957-fce7ab65adbb)

5. 按下Reset Token按鈕，並複製TOKEN，貼到`.env`中的DISCORD_TOKEN="**在這裡貼上您的token**"
   
  ![螢幕擷取畫面 2025-06-02 202038](https://github.com/user-attachments/assets/3dc2b358-e7fa-4551-bb76-0a4f1cffe564)
  
  請不要分享您的TOKEN給別人



### DISCORD_SERVER_ID

1. 確保你的discord有開啟開發者模式(設定>進階>開發者模式)

![螢幕擷取畫面 2025-06-02 202732](https://github.com/user-attachments/assets/554650d0-40d8-4e34-8fed-215903e0714c)

2. 到剛剛加入機器人的伺服器中取得(對著籃框區域按下右鍵)

![螢幕擷取畫面 2025-06-02 203142](https://github.com/user-attachments/assets/889df7b7-112b-4f21-884b-552b034b1fff)

3. 複製伺服器ID，貼到`.env`中的DISCORD_SERVER_ID =**在這裡貼上您的伺服器ID**



### GEMINI_API
1. 前往[Gemini API](https://aistudio.google.com/apikey)，並點下create API
   ![螢幕擷取畫面 2025-06-02 203828](https://github.com/user-attachments/assets/04cdc7be-0121-4b72-b801-9c83e4f91e29)
2. 複製API KEY
   
  ![螢幕擷取畫面 2025-06-02 204040](https://github.com/user-attachments/assets/920d3ba3-c6a6-4316-93f3-43043440e9c1)

3. 貼到`.env`中的GEMINI_API ="**在這裡貼上您的API KEY**"
   
  請不要隨意洩漏您的API，這相當於忘記登出的GMAIL帳號，任何人都可以使用



### SERPAPI_API_KEY
1. 前往[SerpAPI](https://serpapi.com/)，如果你是第一次來請註冊，驗證手機與電子郵件
   
2. 登錄並複製
   
   ![螢幕擷取畫面 2025-06-02 205248](https://github.com/user-attachments/assets/b6ed269c-f804-4aa1-8144-db0d2f7b2117)
   
3. 貼到`.env`中的SERPAPI_API_KEY ="**在這裡貼上您的Your Private API Key**"
  請不要隨意洩漏您的api



### GOOGLE_MAPS_API
開始前提醒您，為了激活90天免費試用，您需要一張信用卡用於註冊
1. 前往[Google Cloud Console](https://console.cloud.google.com/apis/dashboard)
2. 隨便選一個project(可能有Gemini API)
   
  ![螢幕擷取畫面 2025-06-02 210153](https://github.com/user-attachments/assets/33e35a48-6ab3-41cc-9b36-7f6960f77848)

3. 激活Directions api
   
   ![螢幕擷取畫面 2025-06-02 210503](https://github.com/user-attachments/assets/4f08f15d-e8bc-477d-9d1c-c509e0550b5b)
   
   ![螢幕擷取畫面 2025-06-02 210642](https://github.com/user-attachments/assets/268c1b0c-bf05-4f59-a144-a26e860c92df)
   
4. 創建api key
   
   ![螢幕擷取畫面 2025-06-02 210906](https://github.com/user-attachments/assets/c041a638-208a-4e2a-bacc-046b39e40cf4)
   
5. 創建完成後請點擊右側的edited api key
   
   ![螢幕擷取畫面 2025-06-02 211211](https://github.com/user-attachments/assets/af1d3853-2caf-45ba-9f3e-2c35ef3bc060)
   
6. 將API restrictions 切換成Restrict key並勾選Directions api，最後記得按下保存。
   
   ![螢幕擷取畫面 2025-06-02 211354](https://github.com/user-attachments/assets/4ef2fb38-410e-4a84-a71c-737a483e0b71)
   
   ![螢幕擷取畫面 2025-06-02 211450](https://github.com/user-attachments/assets/ea60e6dd-2ea6-43ca-82fc-7958b935533f)
   
8. 點擊show key，並複製粘貼到`.env`中的GOOGLE_MAPS_API ="**在這裡貼上您的API KEY**"
   
    ![螢幕擷取畫面 2025-06-02 214408](https://github.com/user-attachments/assets/2ba93e86-be76-4ce0-9abf-d81058b6a4b5)



### NASA_API

1. 前往[NASA API](https://api.nasa.gov/)，點選get start
2. 誠實填寫您的電子郵件，之後api就會被發送到您的信箱了
3. 複製粘貼到`.env`中的NASA_API ="**在這裡貼上您的NASA API KEY**"


## 執行

1. 在TERMINAL中輸入以下指令
   
    ```bash
    python main.py
    ```
    
2. 如果成功執行terminal 上會有如下輸出

  ![螢幕擷取畫面 2025-06-02 212454](https://github.com/user-attachments/assets/9bdd9672-bf0f-4764-b8af-54bdd303a260)

3. 可以去discord 中測試機器人了喔!!

