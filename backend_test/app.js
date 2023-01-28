const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors());
app.post("/", (req, res) => {
  res.send(`
  Lorem ipsum dolor sit amet. Eos velit quia ut nisi consectetur qui sunt nisi eos neque quia eos beatae sequi 33 illo esse a quos nesciunt. Est sequi omnis vel enim sunt et temporibus illum eum voluptatibus dolor. Aut suscipit perspiciatis qui nostrum quod qui quae quis aut vitae galisum est sapiente consectetur ab aspernatur nemo qui blanditiis tenetur! Ad illo eligendi et esse sequi sit corrupti consequuntur hic maiores dignissimos ut dolores omnis.
  
  Ut ipsum enim et suscipit ducimus qui eveniet nobis qui doloremque ipsam qui enim repellat. Sit amet fuga At repudiandae tenetur eos dolor veniam ex tenetur rerum aut quia magni! Et totam laboriosam eum deleniti vitae ab galisum vero sed recusandae distinctio et repudiandae ipsa aut voluptate alias aut facilis culpa. Et voluptatum dolor quo corrupti necessitatibus quo dolore sint.
  
  Sit consequatur ipsam est voluptates dolores non facilis ipsum aut rerum perspiciatis quo laboriosam debitis. Ut voluptas consequatur et consequatur vitae eum corrupti laboriosam et ipsum dolorem. At quisquam dolores non aliquid molestiae ea sequi omnis ad amet odio eum quia obcaecati! Cum ullam dolores aut quia quae aut autem repellat non similique totam et consequatur doloribus aut eius blanditiis est quasi minus.
  
  Qui galisum natus ut velit voluptas aut enim dolorem et repellendus maiores aut magnam vero aut facere iste rem ducimus excepturi. Eum facere consequatur aut aperiam architecto id facilis enim At dignissimos quia?
  
  Cum iste veritatis ut minima atque vel consequuntur ratione At voluptas autem. Aut dolorem facilis ea nostrum harum et galisum iure et rerum sapiente et aspernatur omnis aut veniam dolorem cum labore illo. Ut quia provident At aliquid soluta ut dignissimos consequatur et reprehenderit rerum aut illum aspernatur eum quae sint ad minus itaque. Et omnis adipisci id atque quisquam eum repellat dolores.
  `);
});

app.listen(3000, () => {
  console.log("Server started on port 3000");
});
