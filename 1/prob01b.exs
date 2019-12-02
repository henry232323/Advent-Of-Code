defmodule Prob01b do
  def sum(file) do
    file
      |> Enum.map(&Integer.parse/1)
      |> Enum.map(&fuel/1)
      |> Enum.sum
  end

  def fuel({m, c}) do
    s = m / 3 - 2
      |> Kernel.trunc
    if (s > 0) do
      s + fuel({s, c})
    else
      0
    end
  end
end

File.stream!("input.txt", [:read])
  |> Prob01b.sum
  |> IO.puts
