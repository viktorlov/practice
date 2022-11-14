dict_ = {"key1": {"key11": {"key111": "value111",
                            "key112": "value112",
                            "sign": False
                            },
                  "key12": {"key121": "value121",
                            "key122": "value122",
                            "sign": False
                            },
                  "key13": {"ket131": "value131",
                            "key132": "value132",
                            "sign": False
                            }}}

fx = lambda x, y: dict_[x][y]['sign'] + 1

print(fx('key1', 'key12'))

print(dict_)
