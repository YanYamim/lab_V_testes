package br.edu.fatec.sjc;

import java.util.ArrayList;
import java.util.List;

public class NumberAscOrder<T extends Number> {

    private final CustomStack<T> stack;

    public NumberAscOrder(CustomStack<T> stack) {
        this.stack = stack;
    }

    /**
     * Retorna os números da pilha em ordem ascendente.
     * @return lista ordenada ascendentemente
     * @throws StackEmptyException se a pilha estiver vazia
     */
    public List<T> sort() throws StackEmptyException {
        if (stack == null || stack.isEmpty()) {
            throw new StackEmptyException();
        }

        List<T> sortedList = new ArrayList<>();

        while (!stack.isEmpty()) {
            sortedList.add(stack.pop());
        }

        sortedList.sort((a, b) -> Double.compare(a.doubleValue(), b.doubleValue()));

        return sortedList;
    }
}
