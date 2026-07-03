function Math(elem)
  if elem.mathtype == "DisplayMath" then
    local trimmed = elem.text:match('^%s*(.-)%s*$')
    -- amsmath disallows \tag inside aligned; move it to just after \end{aligned}
    trimmed = trimmed:gsub('(\\tag%b{})%s*\n%s*\\end{aligned}', '\\end{aligned}\n%1')
    return pandoc.RawInline('latex', '\\begin{equation*}\n' .. trimmed .. '\n\\end{equation*}')
  end
end
