package br.edu.fatec.sjc;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.junit.jupiter.api.extension.ExtendWith;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(MockitoExtension.class)
public class NumberAscOrderTest {

    @Mock
    CalculableStrategy<Double> calculableStrategy;

    private CustomStack<Double> stack;

    @BeforeEach
    void setup() {
        stack = new CustomStack<>(6, calculableStrategy);
    }

    @Test
    void testSortWithSixNumbers() {
        try {
            Mockito.when(calculableStrategy.calculateValue(Mockito.anyDouble()))
                    .thenAnswer(invocation -> invocation.getArgument(0));

            stack.push(45.0);
            stack.push(3.0);
            stack.push(12.0);
            stack.push(8.0);
            stack.push(60.0);
            stack.push(25.0);

            NumberAscOrder<Double> ascOrder = new NumberAscOrder<>(stack);
            List<Double> sorted = ascOrder.sort();

            assertEquals(List.of(3.0, 8.0, 12.0, 25.0, 45.0, 60.0), sorted);
            assertTrue(sorted.get(0) < sorted.get(5));
        } catch (Exception e) {
            fail("Não deveria lançar exceção: " + e.getMessage());
        }
    }

    @Test
    void testSortWithEmptyStackShouldThrowException() {
        NumberAscOrder<Double> ascOrder = new NumberAscOrder<>(stack);
        assertThrows(StackEmptyException.class, ascOrder::sort);
    }
}
