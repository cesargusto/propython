
class Roman
  def romanToInt(str)
    # ...
  end
  def method_missing(methId)
    str = methId.id2name
    romanToInt(str)
  end
end

r = Roman.new
r.iv	»	4
r.xxiii	»	23
r.mm	»	2000
