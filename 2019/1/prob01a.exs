defmodule Prob01a do
  def sum(file) do
    file
      |> Enum.map(&Integer.parse/1)
      |> Enum.map(&fuel/1)
      |> Enum.sum
  end

  def fuel({m, _}) do
    m / 3 - 2
      |> Kernel.trunc
  end
end

File.stream!("input.txt", [:read])
  |> Prob01a.sum
  |> IO.puts
