from utils import LLM
import json

input_str = """
<html>

<body>
    <table>
        <thead>
            <tr>
                <td></td>
                <td> Sample</td>
                <td> SiO2</td>
                <td>TiO2</td>
                <td>AI2O3</td>
                <td>FeO</td>
                <td>MnO</td>
                <td>MgO</td>
                <td>CaO</td>
                <td>Na2O</td>
                <td>K2O</td>
                <td>P205</td>
                <td>cI</td>
                <td> Analytical Total</td>
                <td></td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="8">Changbaishan volcano</td>
                <td rowspan="2">K-a (n=6)</td>
                <td>67.94</td>
                <td>0.36</td>
                <td>14.61</td>
                <td>4.58</td>
                <td>:</td>
                <td>0.13</td>
                <td>1.09</td>
                <td>5.51</td>
                <td>5.78</td>
                <td>:</td>
                <td>-</td>
                <td>95.99</td>
                <td> Mean</td>
            </tr>
            <tr>
                <td>1.31</td>
                <td>0.15</td>
                <td>0.47.</td>
                <td>0.39</td>
                <td>-</td>
                <td>0.14</td>
                <td>0.36</td>
                <td>0.14</td>
                <td>0.15</td>
                <td></td>
                <td>-</td>
                <td>0.50</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">K-b (n=10)</td>
                <td>74.88</td>
                <td>0.20</td>
                <td>10.66</td>
                <td>4.05</td>
                <td>0.08</td>
                <td>0.02</td>
                <td>0.26</td>
                <td>5.32</td>
                <td>4.52</td>
                <td>:</td>
                <td>:</td>
                <td>96.34</td>
                <td>Mean</td>
            </tr>
            <tr>
                <td>0.53</td>
                <td>0.07</td>
                <td>0.36</td>
                <td>0.19</td>
                <td>0.10</td>
                <td>0.03</td>
                <td>0.07</td>
                <td>0.68</td>
                <td>0.19</td>
                <td>-</td>
                <td></td>
                <td>0.72</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">TC-a (n= 3)a</td>
                <td>67.00</td>
                <td>0.46</td>
                <td>15.16</td>
                <td>4.89</td>
                <td>0.10</td>
                <td>0.13</td>
                <td>111</td>
                <td>5.27</td>
                <td>5.87</td>
                <td>-</td>
                <td>-</td>
                <td></td>
                <td>Mean</td>
            </tr>
            <tr>
                <td></td>
                <td>0.12</td>
                <td>0.55</td>
                <td>0.25</td>
                <td>0.11</td>
                <td>0.08</td>
                <td>0.17</td>
                <td>0.46</td>
                <td>0.32</td>
                <td>-</td>
                <td>-</td>
                <td></td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">TC-b (n=15)a</td>
                <td>1.33 74.58</td>
                <td>0.25</td>
                <td>10.90</td>
                <td>4.20</td>
                <td>0.07</td>
                <td>0.06</td>
                <td>0.28</td>
                <td>5.01</td>
                <td>4.66</td>
                <td>-</td>
                <td>:</td>
                <td></td>
                <td> Mean</td>
            </tr>
            <tr>
                <td></td>
                <td>0.10</td>
                <td>2.19</td>
                <td>0.44</td>
                <td>0.06</td>
                <td>0.10</td>
                <td>0.35</td>
                <td>0.61</td>
                <td>0.78</td>
                <td>-</td>
                <td>:</td>
                <td></td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="4">Japan region</td>
                <td rowspan="2">B-Tm-a (n = 18)a</td>
                <td>3.75 66.63</td>
                <td>0.46</td>
                <td>14.86</td>
                <td>5.01</td>
                <td>0.14</td>
                <td>0.24</td>
                <td>1.36</td>
                <td>5.67</td>
                <td>5.42</td>
                <td></td>
                <td></td>
                <td></td>
                <td>Mean</td>
            </tr>
            <tr>
                <td>2.48</td>
                <td>0.39</td>
                <td>1.00</td>
                <td>0.67</td>
                <td>0.20</td>
                <td>0.42</td>
                <td>0.88</td>
                <td>0.64</td>
                <td>0.41</td>
                <td>- -</td>
                <td>: -</td>
                <td></td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">B-Tm-b (n =24)a</td>
                <td>74.79</td>
                <td>0.24</td>
                <td>10.53</td>
                <td>4.19</td>
                <td>0.10</td>
                <td>0.03</td>
                <td>0.28</td>
                <td>5.07</td>
                <td>4.37</td>
                <td></td>
                <td></td>
                <td></td>
                <td>Mean</td>
            </tr>
            <tr>
                <td>1.94</td>
                <td>0.17</td>
                <td>1.04</td>
                <td>0.32</td>
                <td>0.10</td>
                <td>0.07</td>
                <td>0.16</td>
                <td>0.54</td>
                <td>0.47</td>
                <td>-</td>
                <td>-</td>
                <td></td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="4">NGRIP</td>
                <td rowspan="2">QUB-1437a (n=10)b</td>
                <td>68.05</td>
                <td>0.30</td>
                <td>14.86</td>
                <td>4.80</td>
                <td>0.14</td>
                <td>0.12</td>
                <td>1.26</td>
                <td>4.69</td>
                <td>5.76</td>
                <td></td>
                <td></td>
                <td>95.77</td>
                <td> Mean</td>
            </tr>
            <tr>
                <td>2.14</td>
                <td>0.13</td>
                <td>0.89</td>
                <td>0.30</td>
                <td>0.16</td>
                <td>0.11</td>
                <td>0.32</td>
                <td>0.58</td>
                <td>0.47</td>
                <td>- -</td>
                <td>- :</td>
                <td>1.56</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">QUB-1437b (n=6)b</td>
                <td>75.58</td>
                <td>0.20</td>
                <td>10.41</td>
                <td>4.18</td>
                <td>0.08</td>
                <td>0.04</td>
                <td>0.29</td>
                <td>4.57</td>
                <td>4.65</td>
                <td>-</td>
                <td>-</td>
                <td>96.42</td>
                <td> Mean</td>
            </tr>
            <tr>
                <td>2.87</td>
                <td>0.12</td>
                <td>0.76</td>
                <td>0.23</td>
                <td>0.09</td>
                <td>0.07</td>
                <td>0.35</td>
                <td>1.22</td>
                <td>0.43</td>
                <td>-</td>
                <td>-</td>
                <td>1.17.</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="7">NEEM-2011-S1</td>
                <td rowspan="2">QUB-1819a (n=6)</td>
                <td>67.63</td>
                <td>0.39</td>
                <td>14.78</td>
                <td>4.77</td>
                <td>0.17</td>
                <td>0.11</td>
                <td>112</td>
                <td>5.36</td>
                <td>5.48</td>
                <td></td>
                <td></td>
                <td>96.58</td>
                <td>Mean</td>
            </tr>
            <tr>
                <td>1.50</td>
                <td>0.02</td>
                <td>0.97</td>
                <td>0.42</td>
                <td>0.19</td>
                <td>0.08</td>
                <td>0.36</td>
                <td>0.86</td>
                <td>0.36</td>
                <td></td>
                <td>0.18 0.08</td>
                <td>1.86</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td rowspan="2">QUB-1819b (n=4)</td>
                <td>74.74</td>
                <td>0.22</td>
                <td>10.57</td>
                <td>4.07</td>
                <td>0.04</td>
                <td>0.02</td>
                <td>0.29</td>
                <td>5.04</td>
                <td>4.54</td>
                <td>0.00</td>
                <td>0.46</td>
                <td>96.18</td>
                <td> Mean</td>
            </tr>
            <tr>
                <td>0.90</td>
                <td>0.06</td>
                <td>1.02</td>
                <td>0.44</td>
                <td>0.04</td>
                <td>0.02</td>
                <td>0.19</td>
                <td>1.01</td>
                <td>0.52</td>
                <td></td>
                <td>0.05</td>
                <td>4.82</td>
                <td>2 SD</td>
            </tr>
            <tr>
                <td>QUB-1819c (n=1)</td>
                <td>76.53</td>
                <td>0.06</td>
                <td>13.34</td>
                <td>0.57</td>
                <td>0.08</td>
                <td>0.03</td>
                <td>0.81</td>
                <td>3.79</td>
                <td>4.70</td>
                <td>-</td>
                <td>0.08</td>
                <td>94.91</td>
                <td></td>
            </tr>
            <tr>
                <td>QUB-1823a (n=1)</td>
                <td>71.29</td>
                <td>0.46</td>
                <td>14.91</td>
                <td>2.17</td>
                <td>0.08</td>
                <td>0.40</td>
                <td>1.57</td>
                <td>2.71</td>
                <td>3.72</td>
                <td>-</td>
                <td>0.13</td>
                <td>92.49</td>
                <td></td>
            </tr>
            <tr>
                <td>QUB-1823b (n=1)</td>
                <td>77.94</td>
                <td>0.02</td>
                <td>13.49</td>
                <td>0.51</td>
                <td>0.19</td>
                <td>0.05</td>
                <td>0.78</td>
                <td>4.04</td>
                <td>4.74</td>
                <td></td>
                <td>0.11</td>
                <td>94.23</td>
                <td></td>
            </tr>
            <tr>
                <td rowspan="2">GISP2</td>
                <td rowspan="2">Glass B (n=9)c</td>
                <td>69.2</td>
                <td>1.3</td>
                <td>13.5</td>
                <td>5.3</td>
                <td>0</td>
                <td>1.1</td>
                <td>3.2</td>
                <td>2.9</td>
                <td>3.6</td>
                <td></td>
                <td></td>
                <td></td>
                <td> Mean</td>
            </tr>
            <tr>
                <td>1.8</td>
                <td>0.2</td>
                <td>1.1</td>
                <td>0.8</td>
                <td></td>
                <td>0.4</td>
                <td>0.6</td>
                <td>1.1</td>
                <td>0.5</td>
                <td></td>
                <td></td>
                <td></td>
                <td>SD</td>
            </tr>
        </tbody>
    </table>
</body>

</html>
"""


def main():
    llm = LLM()
    llm.usage = "DEMO"
    query = {"question": input_str}
    answer = llm.get_answer_dict(query)

    print(json.dumps(answer, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    from langchain_community.callbacks import get_openai_callback

    with get_openai_callback() as cb:
        main()
    print(f"Total Cost (USD): ${cb.total_cost}")
