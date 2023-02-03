import twint
import json

struct = twint.storage.write.struct

def attempt(until):
  c = twint.Config()
  c.Debug = True
  if until is not None:
    c.Until = until
  c.Username = "Yuugumo_ichi"
  c.Store_object = True
  twint.run.Search(c)

  o = twint.output.tweets_list

  if len(o) == 0:
    return None

  for obj in o:
    _obj_type = obj.__class__.__name__
    if _obj_type == "str":
        _obj_type = "username"
    null, data = struct(obj, c.Custom[_obj_type], _obj_type)

    with open("output/data.json", "a", newline='', encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)
        json_file.write("\n")

  return sorted(o, key = lambda o: o.datetime)[0]

def main():
  last_date = None
  while True:
    print("--------------------------------")
    print(f"last date {last_date}")
    oldest = attempt(last_date)
    if oldest is not None:
      last_date = oldest.datetime[0:-4]
      if last_date == '2015-02-20 02:25:16':
        return

    else:
      print("failed with empty res")



main()


# twint -u wangjie000 -o data6.json --json --until "2020-09-25 00:00:00" --limit 10000 --debug